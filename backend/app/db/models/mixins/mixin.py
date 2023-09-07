from uuid import UUID, uuid4
from typing import Optional
from beanie import Document
from pydantic import model_validator, BaseModel, Field
from datetime import datetime


class UUIDMixin(Document):
    custom_id: UUID = Field(default_factory=uuid4)


class Salary(BaseModel):
    min_level: Optional[float] = Field(None, gt=0)
    max_level: Optional[float] = Field(None, gt=0)
    currency: str = "USD"

    @model_validator(mode="before")
    def salary_max_level(cls, values):
        if values:
            min_level, max_level = values.get("min_level"), values.get("max_level")
            if all((min_level, max_level)) and values.get("max_level") < values.get(
                "min_level"
            ):
                raise ValueError("Maximum salary level mast be higher than minimum")

            return values


class Note(BaseModel):
    content_type: str = Field(default="text", frozen=True)
    note_text: str = Field(..., max_length=250)
    created_at: datetime = Field(default_factory=datetime.utcnow, frozen=True)
