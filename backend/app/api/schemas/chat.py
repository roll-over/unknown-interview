from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ChatRequestSchema(BaseModel):
    employer_id: UUID
    applicant_id: UUID
    vacancy_id: UUID
    cv_id: UUID


class ChatResponseSchema(BaseModel):
    custom_id: UUID
    employer_id: UUID
    applicant_id: UUID
    match_id: UUID


class ChatMessageRequestSchema(BaseModel):
    related_id: UUID
    text: str


class ChatMessageResponseSchema(BaseModel):
    related_id: UUID
    created_at: datetime
    text: str