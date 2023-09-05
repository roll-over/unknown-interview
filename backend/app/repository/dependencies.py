from typing import Annotated
from fastapi import Depends

from .interfaces import AbstractBaseRepository
from .repositories import get_cv_repository, get_vacancy_repository


CVsRepository = Annotated[AbstractBaseRepository, Depends(get_cv_repository)]
VacanciesRepository = Annotated[AbstractBaseRepository, Depends(get_vacancy_repository)]
