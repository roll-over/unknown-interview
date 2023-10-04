from app.db.models.cv import CV
from app.services.repository.interfaces import MongoBeanieRepository
from app.services.repository.services import VacancyCVService


class CVRepositoryModel(MongoBeanieRepository):
    model = CV


def get_cv_repository():
    return VacancyCVService(CVRepositoryModel)
