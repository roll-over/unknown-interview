from app.repository.interfaces import AbstractBaseRepository


class MatchCollectionService:
    def __init__(self, repo_model: AbstractBaseRepository):
        self.repo: AbstractBaseRepository = repo_model()

    async def add_records(self, data):
        return await self.repo.create_many(data)

    async def get_records(self, data_id):
        return await self.repo.fetch_many(data_id)
