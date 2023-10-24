from typing import List

from app.db.models import Chat
from app.services.repository.interfaces import AbstractBaseRepository


class ChatService:
    def __init__(self, repo_model: AbstractBaseRepository):
        self.repo: AbstractBaseRepository = repo_model()

    async def get_chats(self) -> List[Chat]:
        return await self.repo.fetch_all()

    async def create_one(self, data: Chat) -> Chat:
        new_data = self.repo.model(**data)  # !!! Replace after ChatUoV implementation
        return await self.repo.create_one(data=new_data)
