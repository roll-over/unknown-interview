from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, EmailStr

from app.db.models.mixins import Role


class UserResponseSchema(BaseModel):
    custom_id: UUID
    name: str
    role: Role
    email: EmailStr
    created_at: datetime


class UserRequestSchema(BaseModel):
    name: str
    role: Role
    email: EmailStr


class UserDataListResponseSchema(BaseModel):
    vacancies: List[UUID] = None
    cvs: List[UUID] = None


class UserEmailSchema(EmailStr):
    pass
