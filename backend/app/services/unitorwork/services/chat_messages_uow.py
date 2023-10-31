from typing import List
from uuid import UUID

from app.db.models import Chat, ChatMessage
from app.exceptions import RelatedRecordDoesNotExists
from app.services.repository.repositories import (
    chat_message_repo,
    chat_repo,
    cv_repo,
    vacancy_repo,
)


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

    async def create_chat(
            self,
            *,
            cv_id: UUID,
            vacancy_id: UUID,
            match_id: UUID,
    ) -> Chat:
        """Create a new chat with related CV, Vacancy and Match IDs.

        Args:
            cv_id: Related CV ID.
            vacancy_id: Related Vacancy ID.
            match_id: Related Match ID.

        Returns:
            Created chat.
        """
        employer = await self.vacancies.get_one(vacancy_id)
        applicant = await self.cvs.get_one(cv_id)
        data = Chat(
            employer_id=employer.owner_id,
            applicant_id=applicant.owner_id,
            match_id=match_id
        )
        created_chat = await self.chats.create_one(data=data)
        return created_chat

    async def get_chat(self, chat_id: UUID) -> Chat | None:
        """Get a chat from db collection by chat id.

        Args:
            chat_id: ID of a chat.

        Returns:
            Chat (if exists). 
            None otherwise.
        """
        found_chat = await self.chats.get_chat(chat_id=chat_id)
        return found_chat

    async def get_many_chats(self, cv_or_vacancy_id: UUID) -> List[Chat]:
        """Get chats from db collection related to a given cv/vacancy ID.
        
        Args:
            related_id: ID of a related vacancy or cv.

        Returns:
            None if related record (cv/vacancy) does not exists.
            List of the chats (if exists) related to a given cv/vacancy ID.
            Empty list if there no chats related to a given cv/vacancy ID.
        """
        if vacancy := await self.vacancies.get_one(cv_or_vacancy_id):
            search_criteria = {
                "employer_id": vacancy.owner_id
            }
        elif cv := await self.cvs.get_one(cv_or_vacancy_id):
            search_criteria = {
                "applicant_id": cv.owner_id
            }
        else:
            return None
            
        found_chats = await self.chats.get_chats(search_criteria)
        return found_chats

    async def create_message(self, data: ChatMessage) -> ChatMessage:
        """Create a new massage for a given chat.
        
        Args:
            chat_id: ID of a chat you want message to be created for.
        
        Returns:
            Created message.
            
        Raises:
            RelatedRecordDoesNotExists: If a chat with given ID does not exists.
        """
        if self.get_chat(chat_id=data.related_id) is None:
            raise RelatedRecordDoesNotExists

        created_message = await self.messages.create_one(data=data)
        return created_message

    async def get_messages(self, chat_id, page, count) -> List[ChatMessage]:
        """Get a sorted list of all chat messages for a given chat.
        
        Args:
            chat_id: ID of a chat you want messages from.
            
        Returns:
            Sorted list of all messages (if exists) for a given chat.
            Empty list otherwise.
        """
        
        found_messages = await self.messages.get_chat_messages(
            chat_id=chat_id,
            page=page,
            count=count
        )
        return found_messages