from typing import Annotated

from fastapi import Depends

from .interfaces.base import AbstractUnitOfWork
from .services import ChatMessageUoW, ChatNoteUoW, MatchVacancyCVUoW, UserVacancyCVUoW

UVC_dep = Annotated[AbstractUnitOfWork, Depends(UserVacancyCVUoW)]
Match_dep = Annotated[AbstractUnitOfWork, Depends(MatchVacancyCVUoW)]
Chat_dep = Annotated[AbstractUnitOfWork, Depends(ChatMessageUoW)]
Note_dep = Annotated[AbstractUnitOfWork, Depends(ChatNoteUoW)]
