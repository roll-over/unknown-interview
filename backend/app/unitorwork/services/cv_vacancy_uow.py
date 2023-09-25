from contextlib import asynccontextmanager

from app.db.models.mixins import Role
from app.exceptions import UserRoleMismatch
from app.repository.repositories import cv_repo, user_repo, vacancy_repo


class UserVacancyCVUoW:
    def __init__(self):
        self.users = user_repo()
        self.cvs = cv_repo()
        self.vacancies = vacancy_repo()

    @asynccontextmanager
    async def get_collection(self, owner_data, role):
        """Provide access to the appropriate collections based on the role.

        Args:
            owner_data: The owner data object to retrieve the collections for.
            role: The role associated with the owner_data.

        Yields:
            Record_collection and owner_collection specified by role.

        Raises:
            UserRoleMismatch: If the owner_data.role does not match the role.
        """
        match role:
            case Role.applicant if role == owner_data.role:
                record_collection = self.cvs
                owner_collection = owner_data.cvs_list
            case Role.employer if role == owner_data.role:
                record_collection = self.vacancies
                owner_collection = owner_data.vacancies_list
            case _:
                raise UserRoleMismatch

        try:
            yield record_collection, owner_collection
        finally:
            await owner_data.save()

    async def create_new(self, data, *, owner_data, role):
        async with self.get_collection(owner_data=owner_data, role=role) as (
                record_collection,
                owner_collection,
        ):
            new_data = await record_collection.create_one(data, owner_data=owner_data)
            owner_collection.append(new_data.custom_id)

        return new_data

    async def delete_record(self, record_id, *, owner_data, role):
        async with self.get_collection(owner_data=owner_data, role=role) as (
                record_collection,
                owner_collection,
        ):
            deleted_record = await record_collection.delete_one(record_id)
            if deleted_record:
                owner_collection.remove(record_id)

        return deleted_record
