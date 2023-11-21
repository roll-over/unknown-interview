from typing import Any, Dict, List, Union
from uuid import UUID

from beanie import Document
from pydantic import BaseModel

from .base import AbstractBaseRepository


class MongoBeanieRepository(AbstractBaseRepository):
    model: Document = None

    async def fetch_all(self, limit: int = None):
        return await self.model.all().limit(limit).to_list()

    async def fetch_many(
        self,
        data_id: Dict[str, UUID],
        sort: str = None,
        limit: int = None,
        skip: int = None
    ) -> List[Document]:
        return await self.model.find(data_id).sort(sort).limit(limit).skip(skip).to_list()

    async def fetch_one(self, data_id: Dict[str, UUID]) -> Union[Document, None]:
        return await self.model.find_one(data_id)

    async def fetch_random(self) -> Union[Document, None]:
        found_data = await self.model.aggregate([{"$sample": {"size": 1}}]).to_list(1)

        if found_data:
            return found_data.pop()

    async def delete_data(self, data_id: Dict[str, UUID]) -> int:
        records = await self.model.find(data_id).delete()

        return records.deleted_count

    async def create_one(self, data: BaseModel) -> Document:
        new_data: Document = self.model(**data.model_dump())
        await new_data.create()

        return new_data

    async def create_many(self, data: List[BaseModel]) -> List[UUID]:
        prepared_data = [self.model(**value) for value in data]
        return await self.model.insert_many(prepared_data)

    async def update_one(
        self,
        data: Dict[str, Any],
        data_id: Dict[str, UUID]
    ) -> Document:
        found_data = await self.fetch_one(data_id)

        if found_data:
            await found_data.update({"$set": data})

            return found_data
