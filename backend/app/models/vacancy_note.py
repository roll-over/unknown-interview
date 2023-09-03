from uuid import UUID
from typing import List

from app.models.mixin import UUIDMixin, Note


class VacancyNote(UUIDMixin):
    vacancy_id: UUID
    notes: List[Note]

    class Settings:
        name = "vacancy_notes"
