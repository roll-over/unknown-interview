from pydantic import BaseModel, EmailStr


class CreateUserRequestSchema(BaseModel):
    name: str
    email: EmailStr
    password_hash: str


class CreateUserResponseSchema(BaseModel):
    id: str
    name: str
    email: EmailStr
    password_hash: str
