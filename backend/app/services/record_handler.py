from typing import Dict, Union
from uuid import UUID

from app.db.models import CV, Role, User, Vacancy

from .unitorwork import MatchVacancyCVUoW, UserVacancyCVUoW


class RecordHandler:
    """A class that handles record preparation.

    Attributes:
        matches: An instance of MatchVacancyCVUoW for managing matches.
        job_records: An instance of UserVacancyCVUoW for managing job records
                    like CV and Vacancy.
    """

    def __init__(self):
        self.matches = MatchVacancyCVUoW()
        self.job_records = UserVacancyCVUoW()

    async def prepare_record(
        self,
        data: Dict,
        *,
        owner_data: User,
        role: Role,
    ) -> Union[CV | Vacancy]:
        """Prepares a record by creating a new job record and preparing matches.

        Args:
            data: The data for creating new CV or Vacancy record.
            owner_data: The owner data associated with the record.
            role: The role associated with the record.

        Returns:
            The created CV or Vacancy.
        """

        created_record = await self.job_records.create_new(
            data, owner_data=owner_data, role=role
        )
        await self.matches.prepare_matches(
            created_record,
            owner_data=owner_data,
            role=role,
        )

        return created_record

    async def get_matched_record(
            self, owner_data: User, role: Role
    ) -> Union[CV | Vacancy | None]:
        """Return matched record from prepared matches collection.

        Args:
            owner_data: The owner data associated with the record.
            role: The role associated with the record.

        Returns:
            Offer CV or Vacancy if existed, otherwise None
        """
        return await self.matches.get_matches(owner_data, role)

    async def delete_record(
        self,
        record_id: UUID,
        *,
        owner_data: User,
        role: Role,
    ) -> bool:
        deleted_record: bool = await self.job_records.delete_record(
            record_id,
            owner_data=owner_data,
            role=role,
        )
        if deleted_record:
            return await self.matches.delete_matches(
                record_id,
                owner_data=owner_data,
                role=role,
            )
