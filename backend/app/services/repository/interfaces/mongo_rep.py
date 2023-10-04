from .base import AbstractBaseRepository


class MongoBeanieRepository(AbstractBaseRepository):
    model = None

    async def fetch_all(self, limit=None):
        found_data = await self.model.all().limit(limit).to_list()

        return found_data

    async def fetch_many(self, data_id):
        found_data = await self.model.find(data_id).to_list()

        return found_data

    async def fetch_one(self, data_id):
        found_data = await self.model.find_one(data_id)

        return found_data

    async def fetch_random(self):
        found_data = await self.model.aggregate([{"$sample": {"size": 1}}]).to_list(1)

        if found_data:
            return found_data.pop()

    async def delete_one(self, data_id):
        found_data = await self.fetch_one(data_id)
        if found_data:
            await found_data.delete()

            return True

    async def create_one(self, data):
        new_data = self.model(**data.model_dump())
        await new_data.create()

        return new_data

    async def create_many(self, data):
        prepared_data = (match.model_dump() for match in data)
        return await self.model.insert_many(list(prepared_data))

    async def update_one(self, data, data_id):
        found_data = await self.fetch_one(data_id)

        if found_data:
            await found_data.update({"$set": data.model_dump()})

            return found_data
