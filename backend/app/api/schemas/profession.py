from pydantic import BaseModel, Field


class ProfessionSchema(BaseModel):
    name: str = Field(..., max_length=20)
