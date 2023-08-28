from pydantic import EmailStr

from app.models.mixin import UUIDMixin


class User(UUIDMixin):  # inherit from the UUIDMixin, since it generates our identifier
    name: str
    email: EmailStr
    password_hash: str

    class Settings:
        name = "users"  # collection name
