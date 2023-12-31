from .chat_message_repo import get_chat_message_repository as chat_message_repo
from .chat_repo import get_chat_repository as chat_repo
from .cv_repo import get_cv_repository as cv_repo
from .match_repo import get_match_repository as match_repo
from .note_repo import get_note_repository as note_repo
from .profession_repo import get_profession_repository as profession_repo
from .skill_repo import get_skill_repository as skill_repo
from .user_repo import get_user_repository as user_repo
from .vacancy_repo import get_vacancy_repository as vacancy_repo

__all__ = (
    "cv_repo",
    "vacancy_repo",
    "user_repo",
    "profession_repo",
    "skill_repo",
    "match_repo",
    "chat_repo",
    "chat_message_repo",
    "note_repo"
)
