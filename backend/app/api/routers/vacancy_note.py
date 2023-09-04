from uuid import UUID
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.api.schemas.vacancy_note import (
    VacancyNoteRequestSchema,
    VacancyNoteResponseSchema,
)
from app.api.schemas.base import BaseNoteSchema
from app.db.models.mixins.mixin import Note
from app.db.models.vacancy_note import VacancyNote

vacancy_note_router = APIRouter(prefix="/vacancy_note", tags=["Vacancy Notes"])


@vacancy_note_router.post("/", response_model=BaseNoteSchema)
async def add_new_note(note: VacancyNoteRequestSchema):
    vacancy_id = note.vacancy_id
    vacancy_notes = await VacancyNote.find_one({"vacancy_id": vacancy_id})
    note_to_add = Note(note_text=note.note_text)

    if vacancy_notes:
        vacancy_notes.notes.append(note_to_add)
        await vacancy_notes.save()
    else:
        vacancy_notes = VacancyNote(vacancy_id=vacancy_id, notes=[note_to_add])
        await vacancy_notes.create()

    return vacancy_notes.notes[-1]


@vacancy_note_router.get("/{vacancy_id}/", response_model=VacancyNoteResponseSchema)
async def get_vacancy_notes(vacancy_id: UUID):
    vacancy_notes = await VacancyNote.find_one({"vacancy_id": vacancy_id})
    return vacancy_notes


@vacancy_note_router.delete("/{vacancy_id}/", response_class=JSONResponse)
async def delete_vacancy_notes(vacancy_id: UUID):
    vacancy_note = await VacancyNote.find_one({"vacancy_id": vacancy_id})
    if not vacancy_note:
        return JSONResponse(
            content={"error": "There is no Notes with such ID"}, status_code=404
        )

    await vacancy_note.delete()
    return JSONResponse(
        content={"message": "Note deleted successfully"}, status_code=200
    )
