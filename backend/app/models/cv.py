from uuid import UUID, uuid4
from typing import Optional
from pydantic import Field

from app.models.mixin import UUIDMixin, Grade, Profession, Salary, Title


class CV(UUIDMixin):
    cv_owner_id: UUID = Field(
        default_factory=uuid4,
    )
    title: Title
    salary: Optional[Salary] = Field(None)
    grade: Grade
    profession: Profession
    skillset: str

    class Settings:
        name = "CV"
