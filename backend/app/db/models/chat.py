from uuid import UUID

from app.db.models.mixins import UUIDMixin


class Chat(UUIDMixin):
    employer: UUID
    applicant: UUID
    vacancy_id: UUID
    cv_id: UUID
    
    class Settings:
        name = "chats"