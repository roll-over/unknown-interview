from typing import Annotated

from fastapi import Depends

from .interfaces.base import AbstractUnitOfWork
from .services import UserVacancyCVUoW

UVC_dep = Annotated[AbstractUnitOfWork, Depends(UserVacancyCVUoW)]
