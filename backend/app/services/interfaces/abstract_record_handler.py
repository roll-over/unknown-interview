from abc import ABC, abstractmethod
from typing import Type

from app.services.record_handler import RecordHandler


class AbstractRecordHandler(ABC):
    """Abstract class for unit of work with records representation."""

    records: Type[RecordHandler]

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
    async def prepare_record(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_matched_record(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def update_record(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete_record(self, **kwargs):
        raise NotImplementedError
