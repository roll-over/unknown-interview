from typing import Dict, List
from uuid import UUID

from app.db.models import Chat
from app.exceptions import RelatedRecordDoesNotExist
from app.services.repository.interfaces import AbstractBaseRepository


class ChatService:
    def __init__(self, repo_model: AbstractBaseRepository):
        self.repo: AbstractBaseRepository = repo_model()
        
    async def get_chat(self, chat_id: UUID) -> Chat:
        chat = await self.repo.fetch_one({"custom_id": chat_id})
        if chat is None:
            raise RelatedRecordDoesNotExist(record='chat')

        return chat

    async def get_chats(self, search_criteria: Dict[str, UUID]) -> List[Chat]:
        return await self.repo.fetch_many(search_criteria)

    async def create_one(self, data: Chat) -> Chat:
        return await self.repo.create_one(data=data)
