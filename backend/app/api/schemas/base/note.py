from typing import List
from uuid import UUID

from pydantic import BaseModel, Field

from app.db.models.mixins import Note


class NoteRequestSchema(BaseModel):
    related_id: UUID
    note_text: str = Field(..., max_length=250)


class NoteResponseSchema(BaseModel):
    related_id: UUID
    notes: List[Note]


class BaseNoteSchema(Note):
    pass
