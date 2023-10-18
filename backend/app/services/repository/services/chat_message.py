from typing import List
from uuid import UUID

from app.db.models.chat_message import ChatMessage
from app.services.repository.interfaces import AbstractBaseRepository


class ChatMessageService:
    def __init__(self, repo_model: AbstractBaseRepository):
        self.repo: AbstractBaseRepository = repo_model()

    async def get_chat_messages(
        self, chat_id: UUID, page: int, count: int
        ) -> List[ChatMessage]:
        search_criteria = {"related_id": chat_id}
        sort_field = "+created_at"
        offset = page * count
        return await self.repo.fetch_many(
            search_criteria,
            sort_field,
            limit=count,
            skip=offset
        )

    async def create_one(self, data: ChatMessage) -> ChatMessage:
        return await self.repo.create_one(data=data)
