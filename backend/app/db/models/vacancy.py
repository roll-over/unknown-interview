from uuid import UUID, uuid4
from typing import Optional
from pydantic import Field

from app.db.models.mixins.mixin import UUIDMixin, Grade, Profession, Salary, Title


class Vacancy(UUIDMixin):
    owner_id: UUID = Field(
        default_factory=uuid4,
    )
    title: Title
    grade: Grade
    salary: Optional[Salary] = Field(None)
    profession: Profession
    skillset: str

    class Settings:
        name = "Vacancy"
