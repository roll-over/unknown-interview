from datetime import datetime
from uuid import UUID

from pydantic import Field

from app.db.models.mixins import UUIDMixin


class ChatMessage(UUIDMixin):
    related_id: UUID
    created_at: datetime = Field(default_factory=datetime.utcnow, frozen=True)
    text: str
    
    class Settings:
        name = "chat_messages"
