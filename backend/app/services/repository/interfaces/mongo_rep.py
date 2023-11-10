from beanie import Document

from .base import AbstractBaseRepository


class MongoBeanieRepository(AbstractBaseRepository):
    model: Document = None

    async def fetch_all(self, limit=None):
        return await self.model.all().limit(limit).to_list()

    async def fetch_many(self, data_id, sort=None, limit=None, skip=None):
        return await self.model.find(data_id).sort(sort).limit(limit).skip(skip).to_list()

    async def fetch_one(self, data_id):
        return await self.model.find_one(data_id)

    async def fetch_random(self):
        found_data = await self.model.aggregate([{"$sample": {"size": 1}}]).to_list(1)

        if found_data:
            return found_data.pop()

    async def delete_data(self, data_id):
        records = await self.model.find(data_id).delete()

        return records.deleted_count

    async def create_one(self, data):
        new_data = self.model(**data.model_dump())
        await new_data.create()

        return new_data

    async def create_many(self, data):
        prepared_data = [self.model(**value) for value in data]
        return await self.model.insert_many(prepared_data)

    async def update_one(self, data, data_id):
        found_data = await self.fetch_one(data_id)

        if found_data:
            await found_data.update({"$set": data})

            return found_data
