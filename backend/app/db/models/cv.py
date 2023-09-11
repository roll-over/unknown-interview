from typing import Optional
from uuid import UUID

from pydantic import Field

from app.db.models.mixins import Grade, Salary, Title, UUIDMixin
from app.db.models.profession import Profession


class CV(UUIDMixin):
    owner_id: UUID
    title: Title
    salary: Optional[Salary] = Field(None)
    grade: Grade
    profession: Profession
    skillset: str

    class Settings:
        name = "CV"
