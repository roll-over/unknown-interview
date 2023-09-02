from uuid import UUID
from typing import List
from pydantic import BaseModel, Field

from app.models.mixin import Note


class VacancyNoteRequestSchema(BaseModel):
    vacancy_id: UUID
    note_text: str = Field(..., max_length=250)


class VacancyNotesResponseSchema(BaseModel):
    vacancy_id: UUID
    notes: List[Note]
