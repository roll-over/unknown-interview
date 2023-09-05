from app.repository.interfaces import AbstractBaseRepository


class UserService:
    def __init__(self, repo_model: AbstractBaseRepository):
        self.repo: AbstractBaseRepository = repo_model()

    async def create_one(self, data):
        return await self.repo.create_one(data)

    async def get_all_users(self):
        return await self.repo.fetch_all()

    async def delete_user(self, data):
        user_email = data.email
        return await self.repo.delete_one({"email": user_email})
