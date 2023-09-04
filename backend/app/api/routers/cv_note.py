from uuid import UUID
from fastapi import APIRouter

from app.api.schemas.cv_note import (
    CVNoteRequestSchema,
    CVNoteResponseSchema,
)
from app.api.schemas.base import BaseNoteSchema
from app.db.models.cv_note import CVNote
from app.db.models.mixins.mixin import Note


cv_note_router = APIRouter(prefix="/cv_note", tags=["CV Notes"])


@cv_note_router.post(
    "/",
    response_model=BaseNoteSchema,
    summary="Add new HR note to the CV",
)
async def add_new_note(data: CVNoteRequestSchema):
    cv_id = data.cv_id
    cv_notes = await CVNote.find_one({"cv_id": cv_id})
    note_to_add = Note(note_text=data.note_text)

    if cv_notes:
        cv_notes.notes.append(note_to_add)
        await cv_notes.save()
    else:
        cv_notes = CVNote(cv_id=cv_id, notes=[note_to_add])
        await cv_notes.create()

    return cv_notes.notes[-1]


@cv_note_router.get(
    "/{cv_id}",
    response_model=CVNoteResponseSchema,
    summary="Returns all HR notes on the specified CV",
)
async def get_cv_notes(cv_id: UUID):
    cv_notes = await CVNote.find_one({"cv_id": cv_id})
    return cv_notes


@cv_note_router.delete(
    "/{cv_id}",
    summary="Delete all HR notes to the CV",
)
async def delete_cv_notes(cv_id: UUID):
    cv_note = await CVNote.find_one({"cv_id": cv_id})
    if cv_note:
        await cv_note.delete()

        return {"message": "Note deleted successfully"}

    return {"error": "There is no Notes with such ID"}
