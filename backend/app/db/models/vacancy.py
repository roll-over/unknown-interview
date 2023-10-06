from typing import List, Optional
from uuid import UUID

from pydantic import Field

from app.db.models.mixins import Grade, Salary, Title, UUIDMixin
from app.db.models.profession import Profession
from app.db.models.skill import Skill


class Vacancy(UUIDMixin):
    owner_id: UUID
    title: Title
    grade: Grade
    salary: Optional[Salary] = Field(None)
    profession: Profession
    skillset: Optional[List[Skill]]
    extra_info: Optional[str] = Field(None, max_length=500)

    class Settings:
        name = "vacancies"
