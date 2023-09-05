from app.repository.interfaces import AbstractBaseRepository


class VacancyCVService:
    def __init__(self, repo_model: AbstractBaseRepository):
        self.repo: AbstractBaseRepository = repo_model()

    async def create(self, data):
        return await self.repo.create_one(data)

    async def get(self, cv_id):
        return await self.repo.fetch_one(cv_id)

    async def get_random(self):
        return await self.repo.fetch_random()

    async def delete(self, data_id):
        return await self.repo.delete_one(data_id)
