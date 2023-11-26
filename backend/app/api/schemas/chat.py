from typing import List
from uuid import UUID

from pydantic import BaseModel

from .messages import MessageResponseSchema
from .note import NoteResponseSchema


class ChatResponseSchema(BaseModel):
    chat_name: str
    messages: List[MessageResponseSchema]
    notes: List[NoteResponseSchema]


class ChatsResponseSchema(BaseModel):
    chat_id: UUID
    chat_name: str
    last_message: List[MessageResponseSchema]
