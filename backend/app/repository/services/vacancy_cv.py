from app.repository.interfaces import AbstractBaseRepository


class VacancyCVService:
    def __init__(self, repo_model: AbstractBaseRepository):
        self.repo: AbstractBaseRepository = repo_model()

    async def create_one(self, data):
        import sys

        print("-----------------------", data, file=sys.stderr)
        print("-----------------------", type(data), file=sys.stderr)

        return await self.repo.create_one(data)

    async def get_one(self, data_id):
        return await self.repo.fetch_one({"custom_id": data_id})

    async def get_random(self):
        return await self.repo.fetch_random()

    async def delete_one(self, data_id):
        return await self.repo.delete_one({"custom_id": data_id})
