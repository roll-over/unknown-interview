from uuid import UUID

from pydantic import BaseModel

from app.db.engine import database

vacancies_collection = database['vacancies']  # create vacancies collection (table)


# fields that must be in the vacancies collection
class VacancyModel(BaseModel):
    id: UUID = None
    title: str
    owner_id: UUID = None
