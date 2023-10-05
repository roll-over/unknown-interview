from app.exceptions import ForbiddenAction
from app.services.repository.interfaces import AbstractBaseRepository


class VacancyCVService:
    def __init__(self, repo_model: AbstractBaseRepository):
        self.repo: AbstractBaseRepository = repo_model()

    async def create_one(self, data, *, owner_data):
        joined_data = self.repo.model(
            owner_id=owner_data.custom_id,
            **data.model_dump(),
        )
        return await self.repo.create_one(joined_data)

    async def get_one(self, data_id):
        return await self.repo.fetch_one({"custom_id": data_id})

    async def get_many(self, filter_, limit=None):
        return await self.repo.fetch_many(filter_, limit)

    # Удалить потом get_all
    async def get_all(self):
        return await self.repo.fetch_all()

    async def get_random(self):
        return await self.repo.fetch_random()

    async def delete_one(self, data_id):
        return await self.repo.delete_one({"custom_id": data_id})

    async def update_one(self, data, data_id, *, owner_data):
        owner_id = owner_data.custom_id
        cv = await self.get_one(data_id)

        if owner_id == cv.owner_id:
            return await self.repo.update_one(data, {"custom_id": data_id})

        raise ForbiddenAction
