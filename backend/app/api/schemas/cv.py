from uuid import UUID
from app.models.mixin import Salary, Title, Grade, Profession
from typing import Optional
from pydantic import BaseModel


class CVRequestSchema(BaseModel):
    title: Title
    salary: Optional[Salary]
    grade: Grade
    profession: Profession
    skillset: str


class CVResponseSchema(BaseModel):
    custom_id: UUID
    cv_owner_id: UUID
    title: Title
    salary: Optional[Salary]
    grade: Grade
    profession: Profession
    skillset: str
