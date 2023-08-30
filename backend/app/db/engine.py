from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.models.user import User
from app.models.cv import CV
from app.models.vacancy import Vacancy


async def init_db():
    # Create Motor client
    client = AsyncIOMotorClient(
        "mongodb://root:example@unknown_mongo:27017/", uuidRepresentation="standard"
    )

    # Initialize beanie with the User document class and a database
    await init_beanie(database=client.db_name, document_models=[User, CV, Vacancy])
