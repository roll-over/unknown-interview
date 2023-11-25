from typing import Dict, List, Union
from uuid import UUID

from app.api.schemas.note import NotePatchSchema, NoteRequestSchema
from app.db.models import ChatMessage, Note, User

from .unitorwork import ChatMessageUoW, ChatNoteUoW


class ChatHandler:
    """A class that handles record preparation.

    Attributes:
        chats_and_messages: An instance of ChatMessageUoW for managing chat messages.
        notes: An instance of ChatNoteUoW for managing chat notes.
    """

    def __init__(self):
        self.chats_and_messages = ChatMessageUoW()
        self.notes = ChatNoteUoW()

    async def get_chat_data(
            self,
            *,
            current_user: User,
            chat_id: UUID,
            page: int,
            count: int
    ) -> Dict[str, Union[str, List[ChatMessage], List[Note]]]:
        """Prepare chat's data: name, messages and notes.

        Args:
            chat_id: ID of a chat.
            current_user: Authorized user.
            page: Page number.
            count: Number of elements per page.

        Returns:
            Prepared chat data.
        """
        chat_messages = await self.chats_and_messages.fetch_chat(
            user_id=current_user.custom_id,
            chat_id=chat_id,
            page=page,
            count=count,
        )
        chat_notes = await self.notes.get_notes(
            chat_id=chat_id,
            author=current_user,
        )

        return dict(**chat_messages, **chat_notes)

    async def fetch_related_chats(
            self,
            record_id: UUID,
            current_user: User,
    ) -> List[Dict[str, Union[UUID, str]]]:
        """Call UoW method to fetch all chats related to job record.

        Args:
            record_id: ID of a related vacancy or cv.
            current_user: Authorized user.

        Returns:
            List of the prepared data.
        """
        return await self.chats_and_messages.fetch_related_chats(
            record_id=record_id,
            user_id=current_user.custom_id,
        )

    async def create_message(
            self,
            data: ChatMessage,
            author: User,
    ) -> Union[ChatMessage, Exception]:
        """Call UoW method to create new message.

        Args:
            data: Text of message with ID of related chat.
            author: Authorized user.

        Returns:
            Created message.

        Raises:
            RelatedRecordDoesNotExist: If a chat with given ID does not exist.
        """
        return await self.chats_and_messages.create_message(
            data=data,
            author_id=author.custom_id,
        )

    async def add_note(
            self,
            data: NoteRequestSchema,
            author: User,
    ) -> Note:
        """Call UoW method to add new note.

        Args:
            data: New note.
            author: Authorized user, supposed author of the note.

        Returns:
            Created note.
        """
        return await self.notes.add_note(
            data=data,
            author=author,
        )

    async def get_note(
            self,
            note_id: UUID,
            author: User,
    ) -> Note:
        """Call UoW method to fetch on note data.

        Args:
            note_id: ID of the note.
            author: Authorized user, supposed author of the note.

        Returns:
            Note data from database.
        """
        return await self.notes.get_note(
            note_id=note_id,
            author=author,
        )

    async def update_note(
        self,
        data: NotePatchSchema,
        note_id: UUID,
        author: User,
    ) -> Note:
        """Call UoW method to note with new text.

        Args:
            data: New text of the note.
            note_id: ID of the note to be updated.
            author: Authorized user, supposed author of the note.

        Returns:
            Updated note.
        """
        return await self.notes.update_note(
            data=data,
            note_id=note_id,
            author=author,
        )

    async def delete_note(
            self,
            note_id: UUID,
            author: User,
    ) -> int:
        """Call UoW method to delete note from database.

        Args:
            note_id: ID of the note to be updated.
            author: Authorized user, supposed author of the note.

        Returns:
            1 if deleting success, otherwise 0.
        """
        return await self.notes.delete_note(
            note_id=note_id,
            author=author,
        )
