from typing import Dict, Generator, List, Union
from uuid import UUID

from app.db.models import CV, MatchRelation, Role, User, Vacancy
from app.services.repository.repositories import (
    cv_repo,
    match_repo,
    user_repo,
    vacancy_repo,
)


class MatchVacancyCVUoW:
    """A class that handles matching vacancies and CVs.

    Attributes:
        matches: An instance of the match repository.
        cvs: An instance of the CV repository.
        vacancies: An instance of the vacancy repository.
        users: An instance of the user repository.
    """

    def __init__(self):
        self.matches = match_repo()
        self.cvs = cv_repo()
        self.vacancies = vacancy_repo()
        self.users = user_repo()

    async def __get_user_records(
        self, owner_data: User, role: Role
    ) -> Union[List[UUID] | None]:
        """Provide access to the appropriate collections based on the role.

        Args:
            owner_data: The owner data object to retrieve the collections for.
            role: The role associated with flag from endpoint.

        Returns:
            Owner_collection specified by role.
        """
        match role:
            case Role.applicant:
                self.id_type = "cv_id"
                self.opposite_id_type = "vacancy_id"
                self.relation_type = "applicant_relation"
                self.offer_repo = self.vacancies
                self.repo = self.cvs
            case Role.employer:
                self.id_type = "vacancy_id"
                self.opposite_id_type = "cv_id"
                self.relation_type = "employer_relation"
                self.offer_repo = self.cvs
                self.repo = self.vacancies

        user_records = await self.users.get_cv_vacancy_data(owner_data)

        return user_records.get(self.id_type + "s")

    async def __check_match_relation(
        self, record_id: UUID
    ) -> Union[CV | Vacancy | None]:
        """Check the match relation for a given record ID.

        Args:
            record_id: The ID of the record to check the match relation for.

        Returns:
            The record if a match relation is found, None otherwise.
        """
        relations = (MatchRelation.shown, MatchRelation.not_shown)
        request = {self.id_type: record_id}

        for relation in relations:
            request[self.relation_type] = relation
            record = await self.matches.get_records(request, limit=1)

            if record:
                if relation == MatchRelation.not_shown:
                    await self.matches.update_relation(
                        record,
                        self.relation_type,
                        MatchRelation.shown,
                    )
                return record

    async def __get_match(
        self,
        reference_records: List[UUID],
        owner_data: User,
        role: Role,
    ) -> Union[CV | Vacancy | None]:
        """Return matched offer for record depends on role.

        Args:
            reference_records: The reference records to find a match for.
            owner_data: The owner data associated with the records.
            role: The role associated with the records.

        Returns:
            The match if found, otherwise None.
        """
        record_id = reference_records[0]
        match_record = await self.__check_match_relation(record_id)

        if match_record:
            match role:
                case Role.applicant:
                    offer_record_id = match_record.vacancy_id
                case Role.employer:
                    offer_record_id = match_record.cv_id

            return await self.offer_repo.get_one(offer_record_id)

        job_record = await self.repo.get_one(record_id)
        await self.prepare_matches(job_record, owner_data, role)

    async def __filter_records(
        self, record: Union[CV | Vacancy]
    ) -> Union[List[CV] | List[Vacancy]]:
        """Filter records based on specific fields.

        Args:
            record: The record to filter.

        Returns:
            The filtered records from database.
        """
        filter_fields = {
            "grade": record.grade,
            "title": record.title,
        }
        return await self.offer_repo.get_many(filter_fields)

    async def prepare_matches(
        self,
        record: Union[CV | Vacancy],
        owner_data: User,
        role: Role,
    ) -> None:
        """Prepare matches for a given record.

        Args:
            record: The record to prepare matches for.
            owner_data: The owner data associated with the record.
            role: The role associated with the record.
        """
        await self.__get_user_records(owner_data, role)
        filtered_data = await self.__filter_records(record)
        prepared_data = (
            {
                self.id_type: record.custom_id,
                self.opposite_id_type: offer_record.custom_id,
            }
            for offer_record in filtered_data
        )

        checked_data = await self.__remove_existing_matches(prepared_data)
        if checked_data:
            await self.matches.add_records(checked_data)

    async def __remove_existing_matches(
        self, data: Generator[Dict[str, UUID], None, None]
    ) -> List[Dict[str, UUID]]:
        """Check and remove existing matches in the database from the given data.

        Args:
            data: The data to remove existing matches from.

        Returns:
            The data with existing matches removed.
        """
        return [
            record for record in data if await self.matches.get_records(record) is None
        ]

    async def get_matches(
        self, owner_data: User, role: Role
    ) -> Union[CV, Vacancy, None]:
        """Return matches for a given owner data and role

        Args:
            owner_data: The owner data associated with the matches.
            role: The role associated with the matches.

        Returns:
            Matched offer record,
            otherwise if owner haven't exiting jb records - a random offer record.
        """
        reference_records = await self.__get_user_records(owner_data, role)
        if reference_records:
            return await self.__get_match(reference_records, owner_data, role)

        return await self.offer_repo.get_random()
