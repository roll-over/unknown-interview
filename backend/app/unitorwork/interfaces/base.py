from abc import ABC, abstractmethod
from typing import Type

from app.repository.repositories.cv_repo import CVRepositoryModel
from app.repository.repositories.user_repo import UserRepositoryModel
from app.repository.repositories.vacancy_repo import VacancyRepositoryModel


class AbstractUnitOfWork(ABC):
    users: Type[UserRepositoryModel]
    cvs: Type[CVRepositoryModel]
    vacancy: Type[VacancyRepositoryModel]

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *args):
        raise NotImplementedError
