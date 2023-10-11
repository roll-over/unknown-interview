from uuid import UUID

from app.db.models.mixins import UUIDMixin


class Chat(UUIDMixin):
    user_one: UUID
    user_two: UUID
    vacancy_id: UUID
    cv_id: UUID
    
    class Settings:
        name = "chats"