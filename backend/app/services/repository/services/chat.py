from app.services.repository.interfaces import AbstractBaseRepository


class ChatService:
    def __init__(self, repo_model: AbstractBaseRepository):
        self.repo: AbstractBaseRepository = repo_model()

    async def get_chats(self):
        return await self.repo.fetch_all()

    async def create_one(self, data: dict):
        return await self.repo.create_one(data=data)