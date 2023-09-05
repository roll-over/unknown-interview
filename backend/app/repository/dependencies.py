from typing import Annotated
from fastapi import Depends

from .interfaces import AbstractBaseRepository
from .repositories import cv_repo, vacancy_repo, cv_note_repo, vacancy_note_repo


CVsRepository = Annotated[AbstractBaseRepository, Depends(cv_repo)]
VacanciesRepository = Annotated[AbstractBaseRepository, Depends(vacancy_repo)]
CVNotesRepository = Annotated[AbstractBaseRepository, Depends(cv_note_repo)]
VacancyNotesRepository = Annotated[AbstractBaseRepository, Depends(vacancy_note_repo)]
