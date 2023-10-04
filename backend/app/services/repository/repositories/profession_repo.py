from app.db.models.profession import Profession
from app.repository.interfaces import MongoBeanieRepository
from app.repository.services import ProfessionService


class ProfessionRepositoryModel(MongoBeanieRepository):
    model = Profession


def get_profession_repository():
    return ProfessionService(ProfessionRepositoryModel)
