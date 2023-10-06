from abc import ABC, abstractmethod
from typing import Type

from app.services.repository.repositories.cv_repo import CVRepositoryModel
from app.services.repository.repositories.user_repo import UserRepositoryModel
from app.services.repository.repositories.vacancy_repo import VacancyRepositoryModel


class AbstractUnitOfWork(ABC):
    """Abstract class for unit of work representation."""

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

    @abstractmethod
    async def create_new(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def delete_record(self, *args):
        raise NotImplementedError
