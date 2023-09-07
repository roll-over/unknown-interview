from uuid import UUID, uuid4
from typing import Optional
from pydantic import Field

from app.db.models.mixins import UUIDMixin, Grade, Profession, Salary, Title


class CV(UUIDMixin):
    owner_id: UUID
    title: Title
    salary: Optional[Salary] = Field(None)
    grade: Grade
    profession: Profession
    skillset: str

    class Settings:
        name = "CV"
