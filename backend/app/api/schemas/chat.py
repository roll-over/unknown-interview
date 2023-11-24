from datetime import datetime
from typing import List, Optional, Union
from uuid import UUID

from pydantic import BaseModel


class MessageRequestSchema(BaseModel):
    related_id: UUID
    text: str


class MessageResponseSchema(BaseModel):
    custom_id: UUID
    author_id: UUID
    created_at: datetime
    text: str
    own: Union[bool, None]


class ChatResponseSchema(BaseModel):
    chat_name: str
    messages: List[MessageResponseSchema]


class ChatsResponseSchema(BaseModel):
    chat_id: UUID
    chat_name: Optional[str]
    last_message: List[MessageResponseSchema]
