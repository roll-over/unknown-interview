from typing import List

from app.db.models.chat import Chat
from app.services.repository.interfaces import AbstractBaseRepository


class ChatService:
    def __init__(self, repo_model: AbstractBaseRepository):
        self.repo: AbstractBaseRepository = repo_model()

    async def get_chats(self) -> List[Chat]:
        return await self.repo.fetch_all()

    async def create_one(self, data: Chat) -> Chat:
        return await self.repo.create_one(data=data)