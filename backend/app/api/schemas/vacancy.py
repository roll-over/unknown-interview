from uuid import UUID
from app.models.mixin import Salary, Title, Grade, Profession
from typing import Optional
from pydantic import BaseModel


class VacancyRequestSchema(BaseModel):
    title: Title
    grade: Grade
    salary: Optional[Salary]
    profession: Profession
    skillset: str


class VacancyResponseSchema(BaseModel):
    custom_id: UUID
    vacancy_owner_id: UUID
    title: Title
    grade: Grade
    salary: Optional[Salary]
    profession: Profession
    skillset: str
