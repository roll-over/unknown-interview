from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ChatRequestSchema(BaseModel):
    user_one: UUID
    user_two: UUID
    vacancy_id: UUID
    cv_id: UUID


class ChatResponseSchema(BaseModel):
    custom_id: UUID
    user_one: UUID
    user_two: UUID
    vacancy_id: UUID
    cv_id: UUID


class ChatMessageRequestSchema(BaseModel):
    related_id: UUID
    text: str


class ChatMessageResponseSchema(BaseModel):
    related_id: UUID
    created_at: datetime
    text: str