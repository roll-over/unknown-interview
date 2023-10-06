from typing import Dict, Union

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
        await self.matches.prepare_matches(created_record)

        return created_record
