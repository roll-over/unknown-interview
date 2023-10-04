from app.db.models.skill import Skill
from app.services.repository.interfaces import MongoBeanieRepository
from app.services.repository.services import SkillService


class SkillRepositoryModel(MongoBeanieRepository):
    model = Skill


def get_skill_repository():
    return SkillService(SkillRepositoryModel)
