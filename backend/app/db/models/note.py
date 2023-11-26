from datetime import datetime
from uuid import UUID

from pydantic import Field

from app.db.models.mixins import UUIDMixin


class Note(UUIDMixin):
    """Dataclass for the notes.

    Attributes:
        related_id: UUID of a chat related to a note.
        author_id: UUID of the author of a note.
        created_at: datetime object; default factory: utcnow.
        note_text: string of the body of a note.
    """
    related_id: UUID
    author_id: UUID
    created_at: datetime = Field(default_factory=datetime.utcnow)
    note_text: str = Field(..., max_length=500)
    
    class Settings:
        name = "notes"
