from datetime import datetime
from typing import Any, Awaitable, Callable, Dict, List, Union
from uuid import UUID

from app.api.schemas.note import NotePatchSchema, NoteRequestSchema
from app.db.models import Note, User
from app.exceptions import ForbiddenAction, UserNotAuthenticated
from app.services.repository.repositories import (
    chat_repo,
    note_repo,
    user_repo,
)


class ChatNoteUoW:
    """A class that handles chats and chat notes.

    Attributes:
        chats: An instance of the chat repository.
        notes: An instance of the note repository.
        users: An instance of the user repository.
    """

    def __init__(self):
        self.chats = chat_repo()
        self.notes = note_repo()
        self.users = user_repo()

    @staticmethod
    def get_existing_user_id(
            func: Callable[..., Awaitable[Any]]
    ) -> Callable[..., Awaitable[Union[Any, Exception]]]:
        """Check if user exists before allowing access to method.

        Parameters:
            func: Callable[..., Awaitable[Any]]
                The method to be decorated.

        Returns:
            Decorated function with arguments.

        Raises:
            UserNotAuthenticated exception, if the user does not exist.
        """
        async def wrapper(self, *args, **kwargs) -> Union[Any, Exception]:
            try:
                existing_user = await self.users.get_user(kwargs.get('author'))
            except AttributeError:
                return
            if existing_user:
                return await func(
                    self,
                    *args,
                    **kwargs,
                    author_id=existing_user.custom_id,
                )
            raise UserNotAuthenticated

        return wrapper

    async def __check_user_permission(
        self,
        chat_id: UUID,
        user_id: UUID,
    ) -> Union[None, Exception]:
        """Check if user have permission to fetch chat data.

        Args:
            chat_id: Related Chat ID.
            user_id: Related User ID.

        Returns:
            None if user ID match with ID of applicant or employer
        Raises:
            ForbiddenAction if user haven't permission.
            RelatedRecordDoesNotExist if chat not exist in database.
        """
        chat = await self.chats.get_chat(chat_id=chat_id)
        match user_id:
            case chat.applicant_id:
                return
            case chat.employer_id:
                return
            case _:
                raise ForbiddenAction

    @get_existing_user_id
    async def add_note(
        self,
        data: NoteRequestSchema,
        author: User,
        author_id: UUID,
    ) -> Note:
        """Add new note with provided text.

        Args:
            data: New note.
            author: Authorized user, supposed author of the note.
            author_id: ID of authorized user.

        Returns:
            Created note.
        """
        await self.__check_user_permission(
            chat_id=data.related_id,
            user_id=author_id,
        )

        joined_data = self.notes.repo.model(
            author_id=author_id,
            **data.model_dump(),
        )

        return await self.notes.add_note(data=joined_data)

    @get_existing_user_id
    async def get_note(
        self,
        note_id: UUID,
        author: User,
        author_id: UUID,
    ) -> Note:
        """Fetch note by ID from database.

        Args:
            note_id: ID of the note.
            author: Authorized user, supposed author of the note.
            author_id: ID of authorized user.

        Returns:
            Note.
        """
        return await self.notes.get_note(
            note_id=note_id,
            author_id=author_id,
        )

    @get_existing_user_id
    async def get_notes(
        self,
        chat_id: UUID,
        author: User,
        author_id: UUID,
    ) -> Dict[str, List[Note]]:
        """Return all notes for chat specified by ID.

        Args:
            chat_id: ID of the chat.
            author: Authorized user, supposed author of the note.
            author_id: ID of authorized user.

        Returns:
            All notes.

        Raises:
            RelatedRecordDoesNotExist if chat not exist in database.
        """
        await self.__check_user_permission(
            chat_id=chat_id,
            user_id=author_id,
        )

        return {"notes": await self.notes.get_notes(
            query={
                "author_id": author_id,
                "related_id": chat_id,
            })}

    @get_existing_user_id
    async def update_note(
        self,
        data: NotePatchSchema,
        note_id: UUID,
        author: User,
        author_id: UUID,
    ) -> Note:
        """Update note with new text provided.

        Args:
            data: New text of the note.
            note_id: ID of the note to be updated.
            author: Authorized user, supposed author of the note.
            author_id: ID of authorized user.

        Returns:
            Updated note.
        """
        prepared_data = {
            "note_text": data.note_text,
            "created_at": datetime.utcnow(),
        }

        return await self.notes.update_note(
            new_data=prepared_data,
            note_id=note_id,
            author_id=author_id,
        )

    @get_existing_user_id
    async def delete_note(
        self,
        note_id: UUID,
        author: User,
        author_id: UUID,
    ) -> int:
        """Delete note from database.

        Args:
            note_id: ID of the note to be updated.
            author: Authorized user, supposed author of the note.
            author_id: ID of authorized user.

        Returns:
            1 if deleting success, otherwise 0.
        """
        return await self.notes.delete_note(
            note_id=note_id,
            author_id=author_id,
        )
