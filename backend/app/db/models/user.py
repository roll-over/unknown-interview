from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import EmailStr, Field

from app.db.models.mixins import UUIDMixin


class User(UUIDMixin):  # inherit from the UUIDMixin, since it generates our identifier
    name: str
    email: EmailStr
    cvs_list: List[UUID] = Field(default_factory=list)
    vacancies_list: List[UUID] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "users"  # collection name
