from datetime import datetime
from typing import List
from uuid import UUID

from app.api.schemas.note import NotePatchSchema, NoteRequestSchema
from app.db.models import Note
from app.services.repository.interfaces import AbstractBaseRepository


class NoteService:
    def __init__(self, repo_model: AbstractBaseRepository):
        self.repo: AbstractBaseRepository = repo_model()
        
    async def add_note(self, data: NoteRequestSchema) -> Note:
        return await self.repo.create_one(data)
    
    async def get_notes(self, author_id: UUID) -> List[Note]:
        search_criteria = {"author_id": author_id}
        sort_field = "+created_at"
        return await self.repo.fetch_many(
            search_criteria,
            sort_field
        )
    
    async def get_note(self, note_id: UUID) -> Note:
        return await self.repo.fetch_one({"custom_id": note_id})
    
    async def update_note(self, data: NotePatchSchema) -> Note:
        note: Note = await self.get_note(data.custom_id)
        note.note_text = data.updated_text
        note.created_at = datetime.utcnow()
        await note.save()
        
        return note
    
    async def delete_note(self, note_id: UUID) -> Note:
        return await self.repo.delete_data({"custom_id": note_id})
