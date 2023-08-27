from uuid import UUID, uuid4

from beanie import Document
from pydantic import EmailStr, model_validator


class User(Document):
    custom_id: UUID
    name: str
    email: EmailStr
    password_hash: str

    class Settings:
        name = 'users'

    @model_validator(mode='before')
    def generate_uuid(cls, values):
        values['custom_id'] = str(uuid4())
        return values
