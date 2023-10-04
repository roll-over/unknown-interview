from app.db.models.match import MatchCollection
from app.repository.interfaces import MongoBeanieRepository
from app.repository.services import MatchCollectionService


class MatchRepositoryModel(MongoBeanieRepository):
    model = MatchCollection


def get_match_repository():
    return MatchCollectionService(MatchRepositoryModel)
