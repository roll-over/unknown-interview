from uuid import UUID

from pydantic import BaseModel, EmailStr

from app.db.engine import database

users_collection = database['users']  # create users collection (table)


# fields that must be in the users collection
class UserModel(BaseModel):
    id: UUID = None
    name: str
    email: EmailStr
    password_hash: str
