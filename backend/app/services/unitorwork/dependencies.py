from typing import Annotated

from fastapi import Depends

from .interfaces.base import AbstractUnitOfWork
from .services import MatchVacancyCVUoW, UserVacancyCVUoW

UVC_dep = Annotated[AbstractUnitOfWork, Depends(UserVacancyCVUoW)]
Match_dep = Annotated[AbstractUnitOfWork, Depends(MatchVacancyCVUoW)]
