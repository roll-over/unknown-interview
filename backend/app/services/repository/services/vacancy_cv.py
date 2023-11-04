from typing import Any, Awaitable, Callable, Dict, List, Union
from uuid import UUID

from app.db.models import CV, User, Vacancy
from app.exceptions import ForbiddenAction
from app.services.repository.interfaces import AbstractBaseRepository


class VacancyCVService:
    def __init__(self, repo_model: AbstractBaseRepository):
        self.repo: AbstractBaseRepository = repo_model()

    @staticmethod
    def check_owner(
            func: Callable[..., Awaitable[Any]]
    ) -> Callable[..., Awaitable[Union[Any, Exception]]]:
        async def wrapper(self, *args, **kwargs) -> Union[Any, Exception]:
            owner_data = kwargs.get('owner_data')
            record_id = kwargs.get('record_id')
            owner_id = owner_data.custom_id
            record = await self.get_one(record_id)
            try:
                owner_record_id = record.owner_id
            except AttributeError:
                return
            if owner_id == owner_record_id:
                return await func(self, *args, record_id=record_id, owner_data=owner_data)
            raise ForbiddenAction

        return wrapper

    async def create_one(
            self,
            data: Union[CV, Vacancy],
            *,
            owner_data: User,
    ) -> Union[CV, Vacancy]:
        joined_data = self.repo.model(
            owner_id=owner_data.custom_id,
            **data.model_dump(),
        )
        return await self.repo.create_one(joined_data)

    async def get_one(self, data_id: UUID) -> Union[CV, Vacancy]:
        return await self.repo.fetch_one({"custom_id": data_id})

    async def get_many(
            self,
            filter_: Dict[str, str],
            limit: Union[int, None] = None,
    ) -> List[Union[CV, Vacancy]]:
        return await self.repo.fetch_many(filter_, limit=limit)

    async def get_random(self) -> Union[CV, Vacancy]:
        return await self.repo.fetch_random()

    @check_owner
    async def delete_one(self, *, record_id: UUID, owner_data: User) -> bool:
        return await self.repo.delete_data(
            {"custom_id": record_id},
        )

    @check_owner
    async def update_one(
            self,
            data: Union[CV, Vacancy],
            *,
            record_id: UUID,
            owner_data: User,
    ) -> Union[CV, Vacancy]:
        return await self.repo.update_one(
            data,
            {"custom_id": record_id},
        )
