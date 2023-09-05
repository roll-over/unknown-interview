from app.repository.services import VacancyCVService
from app.repository.interfaces import MongoBeanieRepository
from app.db.models.vacancy import Vacancy


class VacancyRepositoryModel(MongoBeanieRepository):
    model = Vacancy


def get_vacancy_repository():
    return VacancyCVService(VacancyRepositoryModel)
