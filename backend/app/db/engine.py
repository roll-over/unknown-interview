from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient('mongodb://root:example@unknown_mongo:27017/')  # async connection to mongodb
database = client['unknown_mongo']  # create db
