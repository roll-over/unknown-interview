from .dependencies import Chat_dep, Match_dep, UVC_dep
from .services import ChatMessageUoW, MatchVacancyCVUoW, UserVacancyCVUoW

__all__ = (
    UVC_dep,
    Match_dep,
    Chat_dep,
    UserVacancyCVUoW,
    MatchVacancyCVUoW,
    ChatMessageUoW,
)
