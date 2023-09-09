from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import settings
from app.db.models.profession import Profession
from app.db.models.user import User
from app.db.models.cv import CV
from app.db.models.vacancy import Vacancy
from app.db.models.cv_note import CVNote
from app.db.models.vacancy_note import VacancyNote


class DatabaseInitializer:
    # Initialize models in database
    __models = [User, CV, CVNote, Vacancy, VacancyNote, Profession]

    def __init__(self, stage, mongodb_url):
        self.__stage = stage
        self.__client = AsyncIOMotorClient(mongodb_url, uuidRepresentation="standard")  # Create Motor client

    async def __init_database(self, stage):
        await init_beanie(
            database=self.__client[f'unknown_mongo_{stage}'],
            document_models=self.__models,
        )

    async def get_database_stage(self):
        match self.__stage:
            case 'dev':
                await self.__init_database('development')
            case 'test':
                await self.__init_database('testing')
            case 'prod':
                await self.__init_database('production')
            case _:
                raise 'Unknown database stage. The stage can be one of: dev, test or prod'


init_db = DatabaseInitializer(stage=settings.STAGE, mongodb_url=settings.ME_CONFIG_MONGODB_URL).get_database_stage()
