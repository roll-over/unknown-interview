from app.db.models import Match
from app.services.repository.interfaces import MongoBeanieRepository
from app.services.repository.services import MatchService


class MatchRepositoryModel(MongoBeanieRepository):
    model = Match


def get_match_repository():
    return MatchService(MatchRepositoryModel)
