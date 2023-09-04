from pydantic import EmailStr

from app.db.models.mixins import UUIDMixin


class User(UUIDMixin):  # inherit from the UUIDMixin, since it generates our identifier
    name: str
    email: EmailStr

    class Settings:
        name = "users"  # collection name
