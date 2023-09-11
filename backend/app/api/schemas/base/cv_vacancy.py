from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from app.api.schemas.profession import ProfessionSchema
from app.api.schemas.skill import SkillSchema
from app.db.models.mixins import Grade, Salary, Title


class RequestBaseSchema(BaseModel):
    title: Title
    salary: Optional[Salary]
    grade: Grade
    profession: ProfessionSchema
    skillset: Optional[List[SkillSchema]]


class ResponseBaseSchema(BaseModel):
    custom_id: UUID
    owner_id: UUID
    title: Title
    salary: Optional[Salary]
    grade: Grade
    profession: ProfessionSchema
    skillset: Optional[List[SkillSchema]]
