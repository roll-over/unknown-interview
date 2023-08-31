from uuid import UUID
from typing import List

from app.models.mixin import UUIDMixin, Note


class CVNote(UUIDMixin):
    cv_id: UUID
    notes: List[Note]

    class Settings:
        name = "CVNotes"
