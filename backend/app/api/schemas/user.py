from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserResponseSchema(BaseModel):
    custom_id: UUID
    name: str
    email: EmailStr
    created_at: datetime


class UserRequestSchema(BaseModel):
    name: str
    email: EmailStr


class UserDataListResponseSchema(BaseModel):
    vacancy_ids: List[UUID] = None
    cv_ids: List[UUID] = None


class UserEmailSchema(EmailStr):
    pass


class UserInfoSchema(BaseModel):
    email: UserEmailSchema
    picture: str
