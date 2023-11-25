from typing import Dict, List, Union
from uuid import UUID

from app.db.models import CV, Chat, ChatMessage, Grade, Profession, User, Vacancy
from app.exceptions import ForbiddenAction, RelatedRecordDoesNotExist
from app.services.repository.repositories import (
    chat_message_repo,
    chat_repo,
    cv_repo,
    match_repo,
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
        self.matches = match_repo()

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
        cv_name = await self.__prepare_chat_name(applicant.grade, applicant.profession)
        vacancy_name = await self.__prepare_chat_name(employer.grade, employer.profession)

        data = Chat(
            employer_id=employer.owner_id,
            employer_chat_name=vacancy_name,
            applicant_id=applicant.owner_id,
            applicant_chat_name=cv_name,
            match_id=match_id,
        )

        return await self.chats.create_one(data=data)

    async def fetch_chat(
            self,
            *,
            current_user: User,
            chat_id: UUID,
            page: int,
            count: int
    ) -> Dict[str, Union[str, List[ChatMessage]]]:
        """Prepare chats data: chat ID, chat name and last message to related chat.

        Args:
            chat_id: ID of a chat.
            current_user: Authorized user.
            page: Page number.
            count: Number of elements per page.

        Returns:
            Prepared chat data.
        """
        chat_name = await self.__get_chat_data(
            chat_id=chat_id,
            current_user_id=current_user.custom_id,
        )
        messages = await self.__get_messages(
            author_id=current_user.custom_id,
            chat_id=chat_id,
            page=page,
            count=count,
        )

        return {
            'chat_name': chat_name,
            'messages': messages,
        }

    async def fetch_related_chats(
            self,
            record_id: UUID,
            current_user: User,
    ) -> List[Dict[str, Union[UUID, str]]]:
        """Prepare chats data: chat ID, chat name and last message to related chat.

        Args:
            record_id: ID of a related vacancy or cv.
            current_user: Authorized user

        Returns:
            List of the prepared data.
        """
        current_user_id = current_user.custom_id
        chats = await self.__fetch_many_chats(
            record_id=record_id,
            user_id=current_user_id,
        )

        return [{
            "chat_id": chat.custom_id,
            "chat_name": await self.__get_chat_data(
                chat.custom_id,
                current_user_id=current_user_id,
            ),
            "last_message": await self.__get_messages(
                author_id=current_user_id,
                chat_id=chat.custom_id,
                last_message=True,
            )
        } for chat in chats]

    async def __check_user_permission(
        self,
        record: Union[CV, Vacancy],
        user_id: UUID,
    ) -> Union[UUID, Exception]:
        """Check user permission to access data.

        Args:
            record: Vacancy or CV.
            user_id: Authorised user, supposed owner of the record.

        Returns:
            UUID of owner, if user have permission, otherwise raise exception.

        Raises:
            ForbiddenAction if user have no permission.
        """
        if record.owner_id == user_id:
            return record.custom_id
        raise ForbiddenAction

    async def __fetch_many_chats(
        self,
        record_id: UUID,
        user_id: UUID,
    ) -> Union[List[Chat], None]:
        """Get chats from db collection related to a given cv/vacancy ID.
        
        Args:
            record_id: ID of a related vacancy or cv.
            user_id: Authorised user, supposed owner of the record.

        Returns:
            None if related record (cv/vacancy) does not exist.
            List of the chats (if exists) related to a given cv/vacancy ID.
            Empty list if there are no chats related to a given cv/vacancy ID.
        """
        vacancy = await self.vacancies.get_one(record_id)
        cv = await self.cvs.get_one(record_id)

        if vacancy or cv:
            query = {'$or': [
                {"vacancy_id": await self.__check_user_permission(
                    record=vacancy,
                    user_id=user_id,
                ) if vacancy else None},
                {"cv_id": await self.__check_user_permission(
                    record=cv,
                    user_id=user_id,
                ) if cv else None},
            ]}
        else:
            raise RelatedRecordDoesNotExist(record="job record")
        related_matches = await self.__fetch_related_matches(query)

        new_query = {"match_id": {"$in": related_matches}}
        return await self.chats.get_chats(new_query)

    async def __fetch_related_matches(
        self,
        query: Dict[str, Union[UUID, None]],
    ) -> List[Union[UUID, None]]:
        """Prepare list of match IDs filtered by CV or Vacancy ID.

        Args:
            query: Filter query contain related CV or Vacancy ID.

        Returns:
            List with match IDs, otherwise empty list.
        """
        matches = await self.matches.get_matches(query)
        return [match.custom_id for match in matches]


    async def create_message(
            self,
            data: ChatMessage,
            *,
            author: User,
    ) -> Union[ChatMessage, Exception]:
        """Create a new message for a given chat.
        
        Args:
            data: The ChatMessage data object.
            author: Author of created message.
        
        Returns:
            Created message.
            
        Raises:
            RelatedRecordDoesNotExist: If a chat with given ID does not exist.
        """
        await self.chats.get_chat(chat_id=data.related_id)

        return await self.messages.create_one(data=data, author_id=author.custom_id)

    async def __get_messages(
            self,
            *,
            author_id: UUID,
            chat_id: UUID,
            page: int = 0,
            count: int = 0,
            last_message: bool = None,
    ) -> List[Union[ChatMessage, None]]:
        """Get a sorted list of all chat messages for a given chat.
        
        Args:
            chat_id: ID of a chat.
            author_id: Author ID of created message.
            page: Page number.
            count: Number of elements per page.
            
        Returns:
            Sorted list of all messages for a given chat.
            Empty list otherwise.
        """
        messages = await self.messages.get_last_message(
                chat_id=chat_id,
            ) if last_message else await self.messages.get_chat_messages(
                chat_id=chat_id,
                page=page,
                count=count
            )

        return [await self.__check_message_author(
            data=message,
            current_user_id=author_id,
        ) for message in messages]

    @staticmethod
    async def __check_message_author(
            data: ChatMessage,
            current_user_id: UUID,
    ) -> ChatMessage:
        """Check if currently authorized user is the author of a message.

        Args:
            data: The ChatMessage object to check.
            current_user_id: ID of the current user.

        Returns:
            The message object with updated 'own' attribute.
        """
        if data.author_id != current_user_id:
            data.own = False
        else:
            data.own = True
        return data

    @staticmethod
    async def __prepare_chat_name(grade: Grade, profession: Profession) -> str:
        """Join grade and profession string.

        Args:
            grade: Enum value of related field in record.
            profession: Value of related field in record.

        Returns:
            Value of the 'name' field for chat.
        """
        return ' '.join(
            value.capitalize() for value in (grade.value, *profession.name.split())
        )

    async def __get_chat_data(
            self,
            chat_id: UUID,
            current_user_id: UUID,
    ) -> Union[str, Exception]:
        """Get chat name.

        Args:
            chat_id: Chat ID.
            current_user_id: Authorized user ID.

        Returns:
            Opposite name of the chat, related by ID of authorized user.

        Raises:
            ForbiddenAction: If user ID doesn't match with ID of employer or applicant.
        """
        chat = await self.chats.get_chat(chat_id=chat_id)

        match current_user_id:
            case chat.applicant_id:
                return chat.employer_chat_name
            case chat.employer_id:
                return chat.applicant_chat_name
            case _:
                raise ForbiddenAction
