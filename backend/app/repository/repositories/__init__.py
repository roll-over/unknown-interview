from .cv_repo import get_cv_repository as cv_repo
from .vacancy_repo import get_vacancy_repository as vacancy_repo
from .cv_note_repo import get_cv_note_repository as cv_note_repo
from .vacancy_note_repo import get_vacancy_note_repository as vacancy_note_repo
from .user_repo import get_user_repository as user_repo
from .profession_repo import get_profession_repository as profession_repo
from .skill_repo import get_skill_repository as skill_repo


__all__ = (
    "cv_repo",
    "vacancy_repo",
    "cv_note_repo",
    "vacancy_note_repo",
    "user_repo",
    "profession_repo",
    "skill_repo",
)
