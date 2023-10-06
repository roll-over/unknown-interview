from contextlib import asynccontextmanager
from typing import AsyncContextManager, Dict, List, Tuple, Union
from uuid import UUID

from app.db.models import CV, Role, User, Vacancy
from app.exceptions import UserRoleMismatch
from app.services.repository.repositories import cv_repo, user_repo, vacancy_repo


class UserVacancyCVUoW:
    """Handle user-job record [CV or Vacancy] unit of work.

    Attributes:
        users: An instance of the user repository.
        cvs: An instance of the CV repository.
        vacancies: An instance of the vacancy repository.
    """

    def __init__(self):
        self.users = user_repo()
        self.cvs = cv_repo()
        self.vacancies = vacancy_repo()

    @asynccontextmanager
    async def get_collection(
        self,
        owner_data: User,
        role: Role,
    ) -> AsyncContextManager[
        Union[Tuple[cv_repo, List[UUID]] | Tuple[vacancy_repo, List[UUID]]]
    ]:
        """Provide access to the appropriate collections based on the role.

        Args:
            owner_data: The owner data object to retrieve the collections for.
            role: The role associated with flag from endpoint.

        Yields:
            Record_collection and owner_collection specified by role.

        Raises:
            UserRoleMismatch: If the owner_data.role does not match the role.
        """
        match role:
            case Role.applicant:
                record_collection = self.cvs
                owner_collection = owner_data.cvs_list
            case Role.employer:
                record_collection = self.vacancies
                owner_collection = owner_data.vacancies_list
            case _:
                raise UserRoleMismatch

        try:
            yield record_collection, owner_collection
        finally:
            await owner_data.save()

    async def create_new(
        self,
        data: Dict[str, Union[CV | Vacancy]],
        *,
        owner_data: User,
        role: Role,
    ) -> Union[CV | Vacancy]:
        """Create a new CV or Vacancy and add id to appropriate user collection.

        Args:
            data: The data for the new record.
            owner_data: The owner data object associated with the record.
            role: The role associated with the record.

        Returns:
            Created CV or Vacancy.
        """
        async with self.get_collection(owner_data=owner_data, role=role) as (
            record_collection,
            owner_collection,
        ):
            new_data = await record_collection.create_one(data, owner_data=owner_data)
            owner_collection.append(new_data.custom_id)

        return new_data

    async def delete_record(
        self,
        record_id: UUID,
        *,
        owner_data: User,
        role: Role,
    ) -> bool:
        """Delete CV or Vacancy record from database and appropriate user collection.

        Args:
            record_id: The ID of the record to delete.
            owner_data: The owner data object associated with the record.
            role: The role associated with the record.

        Returns:
            True if the record was deleted successfully, False otherwise.
        """
        async with self.get_collection(owner_data=owner_data, role=role) as (
            record_collection,
            owner_collection,
        ):
            deleted_record = await record_collection.delete_one(record_id)
            if deleted_record:
                owner_collection.remove(record_id)

        return deleted_record
