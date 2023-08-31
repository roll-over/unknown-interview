from uuid import UUID, uuid4
from enum import Enum
from typing import Optional
from beanie import Document
from pydantic import model_validator, BaseModel, Field


class UUIDMixin(Document):
    custom_id: UUID

    @model_validator(mode='before')
    def generate_uuid(cls, values):
        values['custom_id'] = str(uuid4())
        return values


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


class Title(str, Enum):
    member = "мембер"
    lead = "лид"
    teamlead = "тимлид"
    manager = "менеджер"
    director = "директор"


class Grade(Enum):
    junior = "junior"
    middle = "middle"
    senior = "senior"
    lead = "lead"
    principal = "principal"


class Profession(Enum):
    developer = "разработчик"
    designer = "дизайнер"
    manager = "менеджер"
