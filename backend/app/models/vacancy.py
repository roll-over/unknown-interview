from uuid import UUID

from pydantic import BaseModel


class VacancyModel(BaseModel):
    id: UUID = None
    title: str
    owner_id: UUID = None
