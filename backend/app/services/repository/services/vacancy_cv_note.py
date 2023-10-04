from app.repository.interfaces import AbstractBaseRepository


class VacancyCVNoteService:
    def __init__(self, repo_model: AbstractBaseRepository, sub_repo):
        self.repo: AbstractBaseRepository = repo_model()
        self.sub_repo = sub_repo

    async def add_note(self, data):
        related_id = data.related_id
        existing_notes = await self.get_notes(related_id)
        note_to_add = self.sub_repo(note_text=data.note_text)

        if existing_notes:
            existing_notes.notes.append(note_to_add)
            await existing_notes.save()
        else:
            existing_notes = self.repo.model(
                related_id=related_id,
                notes=[note_to_add],
            )
            await self.repo.create_one(existing_notes)

        return existing_notes.notes[-1]

    async def get_notes(self, data_id):
        return await self.repo.fetch_one({"related_id": data_id})

    async def delete_notes(self, data_id):
        return await self.repo.delete_one({"related_id": data_id})
