from datetime import datetime
from typing import Any, Awaitable, Callable, Dict, List, Union
from uuid import UUID

from app.db.models import Note
from app.exceptions import ForbiddenAction
from app.services.repository.interfaces import AbstractBaseRepository


class NoteService:
    def __init__(self, repo_model: AbstractBaseRepository):
        self.repo: AbstractBaseRepository = repo_model()

    @staticmethod
    def check_author(
            func: Callable[..., Awaitable[Any]]
    ) -> Callable[..., Awaitable[Union[Any, Exception]]]:
        async def wrapper(self, *args, **kwargs) -> Union[Any, Exception]:
            author_id = kwargs.pop('author_id')
            note_id = kwargs.pop('note_id')

            note = await self.repo.fetch_one({"custom_id": note_id})
            try:
                note_author_id = note.author_id
            except AttributeError:
                return
            if author_id == note_author_id:
                return await func(
                    self,
                    *args,
                    **kwargs,
                    note_id=note_id,
                    author_id=author_id,
                )
            raise ForbiddenAction

        return wrapper

    async def add_note(
        self,
        data: Note,
    ) -> Note:

        return await self.repo.create_one(data)

    async def get_notes(
        self,
        query: Dict[str, UUID]
    ) -> List[Note]:
        sort_field = "+created_at"

        return await self.repo.fetch_many(
            query,
            sort_field
        )

    @check_author
    async def get_note(self, note_id: UUID, author_id: UUID) -> Note:
        return await self.repo.fetch_one({"custom_id": note_id})

    @check_author
    async def update_note(
        self,
        new_data: Dict[str, Union[str, datetime]],
        *,
        note_id: UUID,
        author_id: UUID
    ) -> Note:
        return await self.repo.update_one(
            new_data,
            {"custom_id": note_id},
        )

    @check_author
    async def delete_note(self, note_id: UUID, author_id: UUID) -> Note:
        return await self.repo.delete_data({"custom_id": note_id})
