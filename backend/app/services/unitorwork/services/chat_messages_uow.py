from uuid import UUID

from app.db.models import Chat, ChatMessage
from app.services.repository.repositories import cv_repo, vacancy_repo, chat_repo, chat_message_repo


class ChatMessageUoW:
    """A class that handles chats and chat messages.

    Attributes:
        cvs: An instance of the CV repository.
        vacancies: An instance of the vacancy repository.
        chats: An instance of the chat repository.
        messages: An instance of the chat messages repository.
    """

    def __init__(self):
        self.cvs = cv_repo()
        self.vacancies = vacancy_repo()
        self.chats = chat_repo()
        self.messages = chat_message_repo()

    # Chat methods:
    # 1. Create chat:
    async def create_one(
            self,
            *,
            cv_id: UUID,
            vacancy_id: UUID,
            match_id: UUID,
    ) -> Chat:
        """Create new chat with related CV, Vacancy and Match IDs.

        Args:
            cv_id: Related CV ID.
            vacancy_id: Related Vacancy ID.
            match_id: Related Match ID.

        Returns:
            Created chat.
        """
        # a. Get owner_id from CV and Vacancy
        # b. Dumb data to Chat model and fix create_one method in chat repo.
        # c. Chat creating/returning
        pass

    # 2. Fetch one chat from db by chat_id.
    # 3. Fetch many chats from db (filter implementation) by CV_id or Vacancy_id:
    #   a. Check if record exists, otherwise return None
    #   b. Refactor get_chats method from Chat repo:

    # Message methods:
    # 1. Create message
    #   a. Check if chat exists (method fetch_one from Chats above), otherwise raise an error
    #   b. If above is True - create/return new message
    # 2. Fetch all messages by chat_id (sorted) -
    #   method already exists, just need to paste it in UoW and add docstring
