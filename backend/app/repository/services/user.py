from app.exceptions import UserEmailAlreadyExist
from app.repository.interfaces import AbstractBaseRepository


class UserService:
    def __init__(self, repo_model: AbstractBaseRepository):
        self.repo: AbstractBaseRepository = repo_model()

    @staticmethod
    def get_user_email(func):
        def wrapper(self, data):
            user_email = data.email
            return func(self, user_email, data)

        return wrapper

    async def create_one(self, data):
        existing_user = await self.get_user(data)
        if existing_user:
            raise UserEmailAlreadyExist()
        new_user_data = self.repo.model(name=data.name, email=data.email)
        return await self.repo.create_one(new_user_data)

    async def get_all_users(self):
        return await self.repo.fetch_all()

    @get_user_email
    async def get_user(self, user_email, data):
        return await self.repo.fetch_one({"email": user_email})

    @get_user_email
    async def delete_user(self, user_email, data):
        return await self.repo.delete_one({"email": user_email})
