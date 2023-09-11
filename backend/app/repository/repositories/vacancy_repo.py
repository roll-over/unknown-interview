from app.db.models.vacancy import Vacancy
from app.repository.interfaces import MongoBeanieRepository
from app.repository.services import VacancyCVService


class VacancyRepositoryModel(MongoBeanieRepository):
    model = Vacancy


def get_vacancy_repository():
    return VacancyCVService(VacancyRepositoryModel)
