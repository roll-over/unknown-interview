from uuid import UUID

from app.db.models.mixins import UUIDMixin


class Chat(UUIDMixin):
    employer_id: UUID
    applicant_id: UUID
    vacancy_id: UUID
    cv_id: UUID
    
    class Settings:
        name = "chats"