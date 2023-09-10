from uuid import UUID
from typing import List

from app.db.models.mixins import UUIDMixin, Note


class CVNote(UUIDMixin):
    related_id: UUID
    notes: List[Note]

    class Settings:
        name = "CVNotes"
