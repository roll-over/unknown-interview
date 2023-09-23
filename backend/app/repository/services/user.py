from app.db.models.mixins import Role
from app.exceptions import UserEmailAlreadyExist
from app.repository.interfaces import AbstractBaseRepository


class UserService:
    def __init__(self, repo_model: AbstractBaseRepository):
        self.repo: AbstractBaseRepository = repo_model()

    @staticmethod
    def get_user_email(func):
        def wrapper(self, data):
            match data:
                case dict():
                    user_email = data.get("email")
                case str():
                    user_email = data
                case _:
                    user_email = data.email
            return func(self, user_email, data)

        return wrapper

    async def create_one(self, data):
        existing_user = await self.get_user(data)
        if existing_user:
            raise UserEmailAlreadyExist()
        new_user_data = self.repo.model(
            name=data.name,
            email=data.email,
            role=data.role,
        )
        return await self.repo.create_one(new_user_data)

    async def get_all_users(self):
        return await self.repo.fetch_all()

    @get_user_email
    async def get_user(self, user_email, data):
        return await self.repo.fetch_one({"email": user_email})

    @get_user_email
    async def delete_user(self, user_email, data):
        return await self.repo.delete_one({"email": user_email})

    @get_user_email
    async def get_cv_vacancy_data(self, user_email, data):
        collection_type = {
            Role.employer: 'vacancies',
            Role.applicant: 'cvs',
        }

        user_data = await self.get_user(user_email)
        match user_data.role:
            case Role.employer:
                result_list = user_data.vacancies_list
            case Role.applicant:
                result_list = user_data.cvs_list

        return {collection_type.get(user_data.role): result_list}
