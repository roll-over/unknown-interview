from typing import List
from uuid import UUID

from app.db.models.mixins import Note, UUIDMixin


class VacancyNote(UUIDMixin):
    related_id: UUID
    notes: List[Note]

    class Settings:
        name = "vacancy_notes"
