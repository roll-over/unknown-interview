from datetime import datetime
from typing import Union
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
