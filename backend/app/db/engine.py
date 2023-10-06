from beanie import init_beanie
from mongomock_motor import AsyncMongoMockClient
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import settings
from app.db.models.cv import CV
from app.db.models.cv_note import CVNote
from app.db.models.match import Match
from app.db.models.profession import Profession
from app.db.models.skill import Skill
from app.db.models.user import User
from app.db.models.vacancy import Vacancy
from app.db.models.vacancy_note import VacancyNote


async def init_client(db_name):
    return (
        AsyncMongoMockClient()[db_name]
        if settings.IS_TEST
        else AsyncIOMotorClient(
            settings.ME_CONFIG_MONGODB_URL,
            uuidRepresentation="standard",
        )[db_name]
    )


async def __init_beanie(db_name):
    __models = [
        User,
        CV,
        CVNote,
        Vacancy,
        VacancyNote,
        Profession,
        Skill,
        Match,
    ]

    client = await init_client(db_name)
    await init_beanie(
        database=client,
        document_models=__models,
    )
    return client


async def init_database():
    stage = settings.STAGE

    database_stage = {
        "dev": "development",
        "test": "testing",
        "prod": "production",
        "dev_stand": "development_stand",
    }

    if stage not in database_stage:
        raise ValueError(
            """Unknown database stage. The stage can be one of:
            dev, dev_stand, test, or prod"""
        )

    db_name = "unknown_mongo_{stage}".format(stage=database_stage.get(stage))
    __database_client = await __init_beanie(db_name)

    return __database_client


init_db = init_database()
