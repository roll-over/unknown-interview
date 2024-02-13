from contextlib import asynccontextmanager
from typing import Any, AsyncContextManager, Awaitable, Callable, List, Tuple, Union
from uuid import UUID

from app.api.schemas.base import RequestBaseSchema as RecordSchema
from app.db.models import CV, Grade, Profession, Role, User, Vacancy
from app.exceptions import ForbiddenAction, UserRoleMismatch
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
        Union[Tuple[cv_repo, List[UUID]], Tuple[vacancy_repo, List[UUID]]]
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

    @staticmethod
    def __check_existing_record(
            func: Callable[..., Awaitable[Any]]
    ) -> Callable[..., Awaitable[Union[Any, Exception]]]:
        async def wrapper(self, *args, **kwargs) -> Union[Any, Exception]:
            """Check if record exists in user collection.

            Args:
                **kwargs:
                    record_id: ID of record.
                    owner_data: The owner data object associated with the record.

            Raises:
                ForbiddenAction if record not exist in the collection.
            """
            owner_data = kwargs.get('owner_data')
            record_id = kwargs.get('record_id')

            if not any((
                    record_id in (
                            record.record_id for record in owner_data.vacancies_list
                    ),
                    record_id in (
                            record.record_id for record in owner_data.cvs_list
                    ),
            )):
                raise ForbiddenAction
            return await func(self, *args, **kwargs)

        return wrapper

    async def create(
        self,
        data: RecordSchema,
        *,
        owner_data: User,
        role: Role,
    ) -> Union[CV, Vacancy]:
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
            record_name = await self.__prepare_record_name(
                grade=data.grade,
                profession=data.profession,
            )
            new_data = await record_collection.create_one(data, owner_data=owner_data)
            owner_collection.append({
                "name": record_name,
                "record_id": new_data.custom_id,
            })

        return new_data

    @staticmethod
    async def __prepare_record_name(grade: Grade, profession: Profession) -> str:
        """Join grade and profession string.

        Args:
            grade: Enum value of related field in record.
            profession: Value of related field in record.

        Returns:
            Value of the 'name' field for chat.
        """
        return ' '.join(
            value.capitalize() for value in (grade.value, *profession.name.split())
        )

    @__check_existing_record
    async def get(
            self,
            *,
            record_id: UUID,
            owner_data: User,
            role: Role,
    ) -> Union[CV, Vacancy, Exception]:
        """Return existing CV or Vacancy if owner matches.

        Args:
            record_id: The ID of existing record.
            owner_data: The owner data object associated with the record.
            role: The role associated with the record.

        Returns:
            CV or Vacancy

        Raises:
            ForbiddenAction if authorised user is not owner of record.
        """
        async with self.get_collection(owner_data=owner_data, role=role) as (
                record_collection,
                owner_collection,
        ):
            return await record_collection.get_record(
                record_id=record_id,
                owner_data=owner_data,
            )

    @__check_existing_record
    async def update(
        self,
        data: RecordSchema,
        *,
        record_id: UUID,
        owner_data: User,
        role: Role,
    ) -> Union[CV, Vacancy, Exception]:
        """Update existing CV or Vacancy.

        Args:
            data: The data for the record update.
            record_id: The ID of existing record.
            owner_data: The owner data object associated with the record.
            role: The role associated with the record.

        Returns:
            Updated CV or Vacancy.

        Raises:
            ForbiddenAction if authorised user is not owner of record.
        """
        async with self.get_collection(owner_data=owner_data, role=role) as (
            record_collection,
            owner_collection,
        ):
            return await record_collection.update_one(
                data,
                record_id=record_id,
                owner_data=owner_data,
            )

    @__check_existing_record
    async def delete(
        self,
        *,
        record_id: UUID,
        owner_data: User,
        role: Role,
    ) -> int:
        """Delete CV or Vacancy record from database and appropriate user collection.

        Args:
            record_id: The ID of the record to delete.
            owner_data: The owner data object associated with the record.
            role: The role associated with the record.

        Returns:
            Quantity of deleted records if success.
        """
        async with self.get_collection(owner_data=owner_data, role=role) as (
            record_collection,
            owner_collection,
        ):
            deleted_record = await record_collection.delete_one(
                record_id=record_id,
                owner_data=owner_data,
            )
            if deleted_record:
                owner_collection.remove(record_id)

        return deleted_record
