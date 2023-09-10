from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.db.models.mixins import Grade, Salary, Title
from app.db.models.profession import Profession


class RequestBaseSchema(BaseModel):
    title: Title
    salary: Optional[Salary]
    grade: Grade
    profession: Profession
    skillset: str


class ResponseBaseSchema(BaseModel):
    custom_id: UUID
    owner_id: UUID
    title: Title
    salary: Optional[Salary]
    grade: Grade
    profession: Profession
    skillset: str
