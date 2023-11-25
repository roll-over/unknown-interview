from abc import ABC, abstractmethod
from typing import Type

from app.services.chat_handler import ChatHandler


class AbstractChatHandler(ABC):
    """Abstract class for unit of work with records representation."""

    records: Type[ChatHandler]

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *args):
        raise NotImplementedError

    async def get_chat_data(self, *args, **kwargs):
        raise NotImplementedError

    async def fetch_related_chats(self, *args, **kwargs):
        raise NotImplementedError

    async def create_message(self, *args, **kwargs):
        raise NotImplementedError

    async def add_note(self, *args, **kwargs):
        raise NotImplementedError

    async def get_note(self, *args, **kwargs):
        raise NotImplementedError

    async def update_note(self, *args, **kwargs):
        raise NotImplementedError

    async def delete_note(self, *args, **kwargs):
        raise NotImplementedError
