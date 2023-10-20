from typing import Dict, Generator, List, Union
from uuid import UUID

from pymongo import DESCENDING

from app.db.models import CV, Match, MatchRelation, Role, User, Vacancy
from app.exceptions import ForbiddenAction, InvalidRelationAction
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
                self.opposite_relation_type = "employer_relation"
                self.offer_repo = self.vacancies
                self.repo = self.cvs
            case Role.employer:
                self.id_type = "vacancy_id"
                self.opposite_id_type = "cv_id"
                self.relation_type = "employer_relation"
                self.opposite_relation_type = "applicant_relation"
                self.offer_repo = self.cvs
                self.repo = self.vacancies

        user_records = await self.users.get_cv_vacancy_data(owner_data)

        return user_records.get(self.id_type + "s")

    async def __check_match_shown_relation(
            self, record_id: UUID
    ) -> Union[CV | Vacancy | None]:
        """Check the match relation for a given record ID.

        Args:
            record_id: The ID of the record to check the match relation for.

        Returns:
            The record if a match relation is found, None otherwise.
        """
        query = {'$or': [
            {self.id_type: record_id, self.relation_type: MatchRelation.shown},
            {self.id_type: record_id, self.relation_type: MatchRelation.not_shown},
        ]}
        sort = (self.relation_type, DESCENDING)
        record = await self.matches.get_records(query, sort=sort, limit=1)

        if record:
            await self.matches.update_relation(
                record,
                self.relation_type,
                MatchRelation.shown,
            )
            return record

    async def __get_match_for_offer(
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
        match_record = await self.__check_match_shown_relation(record_id)

        if match_record:
            match role:
                case Role.applicant:
                    offer_record_id = match_record.vacancy_id
                case Role.employer:
                    offer_record_id = match_record.cv_id

            return await self.offer_repo.get_one(offer_record_id)

    async def __filter_existing_matches(self, record_id: UUID) -> List[Match]:
        """Filter records based on relation type for further deleting.

        Args:
            record_id: The record_id of related record

        Returns:
            The filtered records from database.
        """
        filter_field = {
            self.id_type: record_id,
            self.opposite_relation_type: MatchRelation.not_shown,
        }
        return await self.matches.get_records(filter_field)

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
            record for record in data if not await self.matches.get_records(record)
        ]

    async def __check_collection_ids(
            self,
            *,
            owner_data: User,
            cv_id: UUID,
            vacancy_id: UUID,
    ) -> Union[str | Exception]:
        """Check if provided CV and Vacancy id exists in user collections.

        Args:
            owner_data: The owner data object to retrieve the collections for.
            cv_id: ID of provided CV
            vacancy_id: ID of provided Vacancy

        Returns:
            Type of match relation
        Raises:
            ForbiddenAction if not id in user collections,
            InvalidRelationAction if user try to change relation to own records.
        """
        user_records = await self.users.get_cv_vacancy_data(owner_data)

        existing_cv = cv_id in user_records.get('cv_ids')
        existing_vacancy = vacancy_id in user_records.get('vacancy_ids')

        if all((existing_cv, existing_vacancy)):
            raise InvalidRelationAction

        elif existing_cv:
            return "applicant_relation"

        elif existing_vacancy:
            return "employer_relation"

        raise ForbiddenAction

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

    async def get_matches(
            self, owner_data: User, role: Role
    ) -> Union[CV | Vacancy | None]:
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
            return await self.__get_match_for_offer(reference_records, owner_data, role)

        return await self.offer_repo.get_random()

    async def check_relation(self, match_record: Match) -> bool:
        """Check applicant and employer relation in record.

        Args:
            match_record: Match record.

        Returns:
            True if relation is equal, False otherwise.
        """
        return all((
            match_record.employer_relation == MatchRelation.liked,
            match_record.applicant_relation == MatchRelation.liked,
        ))

    async def update_relation(
            self,
            *,
            owner_data: User,
            new_relation: MatchRelation,
            cv_id: UUID,
            vacancy_id: UUID,
    ) -> Match:
        """Update applicant or employer relation in match.

        Args:
            owner_data: The owner data associated with the record.
            new_relation: new applicant or employer relation.
            cv_id: CV id,
            vacancy_id: Vacancy id,
            role: The role associated with the record.

        Returns:
            True if relation is equal, False otherwise.
        """
        relation = await self.__check_collection_ids(
            owner_data=owner_data,
            cv_id=cv_id,
            vacancy_id=vacancy_id,
        )
        query = {
            "cv_id": cv_id,
            "vacancy_id": vacancy_id,
        }
        match_record = await self.matches.get_records(query, limit=1)

        if match_record:
            updated_record = await self.matches.update_relation(
                match_record,
                relation,
                new_relation,
            )
        else:
            query.update({
                relation: new_relation,
            })
            updated_record = await self.matches.add_records(query)

        return updated_record

    async def update_match_chat_id(
            self,
            chat_id: UUID,
            match_record: Match,
    ) -> None:
        """Add id of already created chat to match

        Args:
            chat_id: Created chat id.
            match_record: Related match record for update.

        Returns:
            None
        """
        await self.matches.update_chat_id(
            match_record=match_record,
            chat_id=chat_id,
        )

    async def delete_matches(
            self,
            *,
            owner_data: User,
            role: Role,
            record_id: UUID,
            record_deleted: bool = None,
    ) -> int:
        """Delete all matches which contain already deleted record, specified by record_id

        Args:
            record_id: id job record, for further handling.
            owner_data: The owner data associated with the matches.
            role: The role associated with the matches.
            record_deleted: Flag that job record fully deleted

        Returns:
            Quantity of deleted records if success.
        """
        await self.__get_user_records(owner_data, role)
        if record_deleted:
            data_to_delete = {self.id_type: record_id}
        else:
            not_shown_matches = await self.__filter_existing_matches(record_id)
            match_ids = (match.custom_id for match in not_shown_matches)
            data_to_delete = {"custom_id": {"$in": match_ids}}

        return await self.matches.delete_matches(data_to_delete)
