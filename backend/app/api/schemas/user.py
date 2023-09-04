from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserResponseSchema(BaseModel):
    custom_id: UUID
    name: str
    email: EmailStr


class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr
