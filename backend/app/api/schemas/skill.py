from pydantic import BaseModel, Field


class SkillSchema(BaseModel):
    name: str = Field(..., max_length=20)
