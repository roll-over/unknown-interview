from datetime import datetime

from pydantic import EmailStr, Field

from app.db.models.mixins import UUIDMixin


class User(UUIDMixin):  # inherit from the UUIDMixin, since it generates our identifier
    name: str
    email: EmailStr
    created_at: datetime = Field(default_factory=datetime.utcnow, frozen=True)

    class Settings:
        name = "users"  # collection name
