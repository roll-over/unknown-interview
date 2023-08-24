from pydantic import BaseModel, EmailStr

from app.db.engine import db

users = db['users']  # create users collection (table)


#  fields that must be in the users collection
class UserModel(BaseModel):
    name: str
    email: EmailStr
    password_hash: str
