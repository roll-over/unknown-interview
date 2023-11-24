from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class NoteRequestSchema(BaseModel):
    related_id: UUID
    note_text: str = Field(..., max_length=500)


class NoteResponseSchema(BaseModel):
    custom_id: UUID
    related_id: UUID
    created_at: datetime
    note_text: str


# class NotePatchSchema(BaseModel):
#     updated_text: str = Field(..., max_length=500)

class NotePatchSchema(BaseModel):
    note_text: str = Field(..., max_length=500)
