from uuid import UUID, uuid4
from typing import Optional
from pydantic import Field

from app.db.models.mixins import UUIDMixin, Grade, Profession, Salary, Title


class Vacancy(UUIDMixin):
    owner_id: UUID
    title: Title
    grade: Grade
    salary: Optional[Salary] = Field(None)
    profession: Profession
    skillset: str

    class Settings:
        name = "Vacancy"
