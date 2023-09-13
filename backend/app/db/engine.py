from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.config import settings
from app.db.models.cv import CV
from app.db.models.cv_note import CVNote
from app.db.models.profession import Profession
from app.db.models.skill import Skill
from app.db.models.user import User
from app.db.models.vacancy import Vacancy
from app.db.models.vacancy_note import VacancyNote

__models = [User, CV, CVNote, Vacancy, VacancyNote, Profession, Skill]
__database_url: str = settings.ME_CONFIG_MONGODB_URL
__database_stage: str = settings.STAGE
__database_client: AsyncIOMotorDatabase = None


async def init_client(db_name):
    global __database_client
    global __database_url

    __database_client = AsyncIOMotorClient(
        __database_url,
        uuidRepresentation="standard",
    )[db_name]

    return __database_client


async def __init_beanie(db_name):
    global __models

    client = await init_client(db_name)
    await init_beanie(
        database=client,
        document_models=__models,
    )


async def init_database(stage=__database_stage):
    global __database_client

    database_stage = {
        "dev": "development",
        "test": "testing",
        "prod": "production",
    }

    if stage not in database_stage:
        raise ValueError(
            "Unknown database stage. The stage can be one of: dev, test, or prod"
        )

    db_name = "unknown_mongo_{stage}".format(stage=database_stage.get(stage))
    await __init_beanie(db_name)

    return __database_client


init_db = init_database()
