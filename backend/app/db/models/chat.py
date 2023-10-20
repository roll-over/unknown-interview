from uuid import UUID

from app.db.models.mixins import UUIDMixin


class Chat(UUIDMixin):
    employer_id: UUID
    applicant_id: UUID
    match_id: UUID
    
    class Settings:
        name = "chats"
