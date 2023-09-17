from datetime import datetime
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


class UserEmailSchema(EmailStr):
    pass
