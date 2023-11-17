from uuid import UUID

from app.db.models.mixins import UUIDMixin


class Chat(UUIDMixin):
    employer_id: UUID
    employer_chat_name: str
    applicant_id: UUID
    applicant_chat_name: str
    match_id: UUID

    class Settings:
        name = "chats"
