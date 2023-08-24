from pydantic import BaseModel, EmailStr


class UserCreateResponseSchema(BaseModel):
    name: str
    email: EmailStr


# or inherit from a UserModel and exclude password_hash

# from app.models.user import UserModel
# class UserCreateResponseSchema(UserModel):
#     class Config:
#         exclude = ['password_hash']
