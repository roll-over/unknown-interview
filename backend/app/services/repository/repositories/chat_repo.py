from app.db.models.chat import Chat
from app.services.repository.interfaces import MongoBeanieRepository
from app.services.repository.services.chat import ChatService


class ChatRepositoryModel(MongoBeanieRepository):
    model = Chat


def get_chat_repository():
    return ChatService(ChatRepositoryModel)