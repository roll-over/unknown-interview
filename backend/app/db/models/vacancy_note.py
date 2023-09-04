from uuid import UUID
from typing import List

from app.db.models.mixins.mixin import UUIDMixin, Note


class VacancyNote(UUIDMixin):
    related_id: UUID
    notes: List[Note]

    class Settings:
        name = "vacancy_notes"
