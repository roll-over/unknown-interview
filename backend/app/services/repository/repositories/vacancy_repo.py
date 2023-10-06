from app.db.models.vacancy import Vacancy
from app.services.repository.interfaces import MongoBeanieRepository
from app.services.repository.services import VacancyCVService


class VacancyRepositoryModel(MongoBeanieRepository):
    model = Vacancy


def get_vacancy_repository():
    return VacancyCVService(VacancyRepositoryModel)
