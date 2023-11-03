from typing import Union
from uuid import UUID

from app.api.schemas.base import RequestBaseSchema as RecordSchema
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
            data: RecordSchema,
            *,
            owner_data: User,
            role: Role,
    ) -> Union[CV, Vacancy]:
        """Prepares a record by creating a new job record and preparing matches.

        Args:
            data: The data for creating new CV or Vacancy record.
            owner_data: The owner data associated with the record.
            role: The role associated with the record.

        Returns:
            The created CV or Vacancy.
        """

        created_record = await self.job_records.create(
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
    ) -> Union[CV, Vacancy, None]:
        """Return matched record from prepared matches collection.

        Args:
            owner_data: The owner data associated with the record.
            role: The role associated with the record.

        Returns:
            Offer CV or Vacancy if existed, otherwise None
        """
        return await self.matches.get_matches(owner_data, role)

    async def update_record(
            self,
            new_record_data: RecordSchema,
            *,
            record_id: UUID,
            owner_data: User,
            role: Role,
    ) -> Union[CV, Vacancy, Exception]:
        """Update CV or Vacancy record and related matches,
            delete related matches if they're not already shown.

        Args:
            new_record_data: The data for the record update.
            record_id: The ID of the record to delete.
            owner_data: The owner data object associated with the record.
            role: The role associated with the record.

        Returns:
            Updated CV or Vacancy, or Exception if raised
        """
        await self.matches.delete_matches(
            record_id=record_id,
            owner_data=owner_data,
            role=role,
        )
        updated_record = await self.job_records.update(
            new_record_data, owner_data=owner_data, role=role, record_id=record_id
        )
        await self.matches.prepare_matches(
            updated_record,
            owner_data=owner_data,
            role=role,
        )

        return updated_record

    async def delete_record(
            self,
            *,
            record_id: UUID,
            owner_data: User,
            role: Role,
    ) -> int:
        """Delete CV or Vacancy record from database & appropriate user collection,
            delete related matches.

        Args:
            record_id: The ID of the record to delete.
            owner_data: The owner data object associated with the record.
            role: The role associated with the record.

        Returns:
            Quantity of deleted records if success.
        """
        deleted_record = await self.job_records.delete(
            record_id=record_id,
            owner_data=owner_data,
            role=role,
        )
        if deleted_record:
            await self.matches.delete_matches(
                record_id=record_id,
                owner_data=owner_data,
                role=role,
                record_deleted=True,
            )
        return deleted_record
