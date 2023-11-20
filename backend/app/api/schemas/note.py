from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class NoteRequestSchema(BaseModel):
    
    #chat_id
    related_id: UUID
    
    author_id: UUID
    note_text: str = Field(..., max_length=500)

class NoteResponseSchema(BaseModel):
    #note_id
    custom_id: UUID
    
    #chat_id
    related_id: UUID
    
    author_id: UUID
    created_at: datetime
    note_text: str

class NotePatchSchema(BaseModel):
    #note_id
    custom_id: UUID

    updated_text: str = Field(..., max_length=500)
