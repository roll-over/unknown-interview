from app.db.models.profession import Profession
from app.services.repository.interfaces import MongoBeanieRepository
from app.services.repository.services import ProfessionService


class ProfessionRepositoryModel(MongoBeanieRepository):
    model = Profession


def get_profession_repository():
    return ProfessionService(ProfessionRepositoryModel)
