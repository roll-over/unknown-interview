from .match import MatchCollectionService
from .profession import ProfessionService
from .skill import SkillService
from .user import UserService
from .vacancy_cv import VacancyCVService
from .vacancy_cv_note import VacancyCVNoteService

__all__ = (
    "VacancyCVService",
    "VacancyCVNoteService",
    "UserService",
    "ProfessionService",
    "SkillService",
    "MatchCollectionService",
)
