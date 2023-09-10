from uuid import UUID
from typing import Optional
from pydantic import Field

from app.db.models.mixins import UUIDMixin, Grade, Salary, Title
from app.db.models.profession import Profession


class Vacancy(UUIDMixin):
    owner_id: UUID
    title: Title
    grade: Grade
    salary: Optional[Salary] = Field(None)
    profession: Profession
    skillset: str

    class Settings:
        name = "Vacancy"
