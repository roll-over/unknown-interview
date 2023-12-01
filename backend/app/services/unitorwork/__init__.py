from .dependencies import Chat_dep, Match_dep, Note_dep, UVC_dep
from .services import ChatMessageUoW, ChatNoteUoW, MatchVacancyCVUoW, UserVacancyCVUoW

__all__ = (
    UVC_dep,
    Match_dep,
    Chat_dep,
    Note_dep,
    UserVacancyCVUoW,
    MatchVacancyCVUoW,
    ChatMessageUoW,
    ChatNoteUoW,
)
