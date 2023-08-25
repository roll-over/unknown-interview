from uuid import UUID

from pydantic import BaseModel


class VacancyCreateResponseSchema(BaseModel):
    id: UUID
    title: str
    owner_id: UUID
