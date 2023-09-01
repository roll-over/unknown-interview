from uuid import UUID
from app.models.mixin import Note
from typing import List
from pydantic import BaseModel, Field


class CVNoteRequestSchema(BaseModel):
    cv_id: UUID
    note_text: str = Field(..., max_length=250)


class CVNotesResponseSchema(BaseModel):
    cv_id: UUID
    notes: List[Note]
