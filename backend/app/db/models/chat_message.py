from datetime import datetime
from typing import Union
from uuid import UUID

from pydantic import Field

from app.db.models.mixins import UUIDMixin


class ChatMessage(UUIDMixin):
    related_id: UUID
    author_id: UUID
    created_at: datetime = Field(default_factory=datetime.utcnow, frozen=True)
    text: str = Field(..., max_length=500)
    own: Union[bool, None] = Field(default=None)

    class Settings:
        name = "chat_messages"
