from abc import ABC, abstractmethod
from typing import Type

from app.services.relation_handler import RelationHandler


class AbstractRelationHandler(ABC):
    """Abstract class for unit of work with chats representation."""

    records: Type[RelationHandler]

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
    async def update_match_relation(self, *args):
        raise NotImplementedError
