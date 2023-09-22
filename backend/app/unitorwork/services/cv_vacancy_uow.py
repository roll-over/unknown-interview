from app.db.models.mixins import Role
from app.repository.repositories import cv_repo, user_repo, vacancy_repo


class UserVacancyCVUoW:
    def __init__(self):
        self.users = user_repo()
        self.cvs = cv_repo()
        self.vacancy = vacancy_repo()

    async def create_new(self, data, *, owner_data, role):
        match owner_data.role:
            case Role.applicant if role == 'applicant':
                new_data = await self.cvs.create_one(data, owner_data=owner_data)
                owner_data.cvs_list.append(new_data.custom_id)
            case Role.employer if role == 'employer':
                new_data = await self.vacancy.create_one(data, owner_data=owner_data)
                owner_data.vacancies_list.append(new_data.custom_id)
            case _:
                return {'message': "The user role does not match the record type"}

        await owner_data.save()

        return new_data
