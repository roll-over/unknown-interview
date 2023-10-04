from app.repository.interfaces import AbstractBaseRepository


class ProfessionService:
    def __init__(self, repo_model: AbstractBaseRepository):
        self.repo: AbstractBaseRepository = repo_model()

    async def get_all_professions(self, limit=None):
        return await self.repo.fetch_all(limit)

    async def create_one(self, data):
        return await self.repo.create_one(data)
