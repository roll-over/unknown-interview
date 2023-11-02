from typing import List, Union
from uuid import UUID

from app.db.models import Chat, ChatMessage
from app.exceptions import RelatedRecordDoesNotExist
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
        return await self.chats.create_one(data=data)

    async def get_chat(self, chat_id: UUID) -> Union[Chat, None]:
        """Get a chat from db collection by chat id.

        Args:
            chat_id: ID of a chat.

        Returns:
            Chat (if exist). 
            None otherwise.
        """
        return await self.chats.get_chat(chat_id=chat_id)

    async def get_many_chats(self, record_id: UUID) -> Union[List[Chat], None]:
        """Get chats from db collection related to a given cv/vacancy ID.
        
        Args:
            record_id: ID of a related vacancy or cv.

        Returns:
            None if related record (cv/vacancy) does not exist.
            List of the chats (if exist) related to a given cv/vacancy ID.
            Empty list if there no chats related to a given cv/vacancy ID.
        """
        vacancy = await self.vacancies.get_one(record_id)
        cv = await self.cvs.get_one(record_id)

        if vacancy or cv:
            query = {'$or': [
                {"employer_id": vacancy.owner_id if vacancy else None},
                {"applicant_id": cv.owner_id if cv else None},
            ]}

        return await self.chats.get_chats(query)

    async def create_message(self, data: ChatMessage) -> Union[ChatMessage, Exception]:
        """Create a new massage for a given chat.
        
        Args:
            data: The ChatMessage data object.
        
        Returns:
            Created message.
            
        Raises:
            RelatedRecordDoesNotExist: If a chat with given ID does not exist.
        """
        if self.get_chat(chat_id=data.related_id) is None:
            raise RelatedRecordDoesNotExist

        return await self.messages.create_one(data=data)

    async def get_messages(
        self, 
        chat_id: UUID, 
        page: int, 
        count: int
        ) -> List[ChatMessage]:
        """Get a sorted list of all chat messages for a given chat.
        
        Args:
            chat_id: ID of a chat.
            page: # of a page.
            count: # of elements per page.
            
        Returns:
            Sorted list of all messages for a given chat.
            Empty list otherwise.
        """

        return await self.messages.get_chat_messages(
            chat_id=chat_id,
            page=page,
            count=count
        )
