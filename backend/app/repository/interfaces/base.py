from abc import ABC, abstractmethod


class AbstractBaseRepository(ABC):
    @abstractmethod
    async def fetch_all(self):
        raise NotImplementedError

    @abstractmethod
    async def fetch_one(self, data_id):
        raise NotImplementedError

    @abstractmethod
    async def fetch_random(self):
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, data_id):
        raise NotImplementedError

    @abstractmethod
    async def create_one(self, data):
        raise NotImplementedError
