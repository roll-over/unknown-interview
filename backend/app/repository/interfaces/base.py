from abc import ABC, abstractmethod


class AbstractBaseRepository(ABC):
    @abstractmethod
    async def fetch_all(self, limit):
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

    @abstractmethod
    async def update_one(self, data, data_id):
        raise NotImplementedError
