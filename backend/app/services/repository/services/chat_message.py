from typing import List
from uuid import UUID

from app.db.models import ChatMessage
from app.services.repository.interfaces import AbstractBaseRepository


class ChatMessageService:
    sort_field = "+created_at"

    def __init__(self, repo_model: AbstractBaseRepository):
        self.repo: AbstractBaseRepository = repo_model()

    async def get_chat_messages(
            self,
            *,
            chat_id: UUID,
            page: int,
            count: int,
    ) -> List[ChatMessage]:
        search_criteria = {"related_id": chat_id}
        offset = page * count

        return await self.repo.fetch_many(
            search_criteria,
            self.sort_field,
            limit=count,
            skip=offset
        )

    async def get_last_message(
            self,
            *,
            chat_id: UUID,
    ) -> List[ChatMessage]:
        search_criteria = {"related_id": chat_id}

        last_message = await self.repo.fetch_many(
            search_criteria,
            self.sort_field,
        )

        return [last_message.pop()] if last_message else []

    async def create_one(
            self,
            data: ChatMessage,
            *,
            author_id: UUID,
    ) -> ChatMessage:
        joined_data = self.repo.model(
            author_id=author_id,
            **data.model_dump(),
        )
        return await self.repo.create_one(joined_data)
