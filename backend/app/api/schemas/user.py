from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserCreateResponseSchema(BaseModel):
    custom_id: UUID
    name: str
    email: EmailStr


class UserCreateRequestSchema(BaseModel):
    name: str
    email: EmailStr
    password_hash: str
