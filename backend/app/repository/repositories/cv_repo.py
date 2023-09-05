from app.repository.services import VacancyCVService
from app.repository.interfaces import MongoBeanieRepository
from app.db.models.cv import CV


class CVRepositoryModel(MongoBeanieRepository):
    model = CV


def get_cv_repository():
    return VacancyCVService(CVRepositoryModel)
