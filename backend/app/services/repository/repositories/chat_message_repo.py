from app.db.models.chat_message import ChatMessage
from app.services.repository.interfaces import MongoBeanieRepository
from app.services.repository.services.chat_message import ChatMessageService


class ChatMessageRepositoryModel(MongoBeanieRepository):
    model = ChatMessage


def get_chat_message_repository():
    return ChatMessageService(ChatMessageRepositoryModel)
