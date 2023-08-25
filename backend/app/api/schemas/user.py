from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserCreateResponseSchema(BaseModel):
    id: UUID
    name: str
    email: EmailStr
