from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.db.models.user import User
from app.db.models.cv import CV
from app.db.models.vacancy import Vacancy
from app.db.models.cv_note import CVNote
from app.db.models.vacancy_note import VacancyNote


async def init_db():
    # Create Motor client
    client = AsyncIOMotorClient(
        "mongodb://root:example@unknown_mongo:27017/", uuidRepresentation="standard"
    )

    # Initialize beanie with the User document class and a database
    await init_beanie(
        database=client.db_name,
        document_models=[User, CV, CVNote, Vacancy, VacancyNote],
    )
