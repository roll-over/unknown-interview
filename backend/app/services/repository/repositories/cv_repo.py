from app.db.models.cv import CV
from app.repository.interfaces import MongoBeanieRepository
from app.repository.services import VacancyCVService


class CVRepositoryModel(MongoBeanieRepository):
    model = CV


def get_cv_repository():
    return VacancyCVService(CVRepositoryModel)
