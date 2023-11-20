from typing import List
from uuid import UUID

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.api.schemas.note import NotePatchSchema, NoteRequestSchema, NoteResponseSchema
from app.services.repository import NotesRepository

note_router = APIRouter(prefix="/notes", tags=["Notes"])

@note_router.post(
    "/add_note",
    response_model=NoteResponseSchema,
    summary="Post a new note."
)
async def add_note(Note: NotesRepository, data: NoteRequestSchema):
    return await Note.add_note(data)

@note_router.get(
    "/{note_id}",
    response_model=NoteResponseSchema,
    summary="Get a note for a given note ID."
)
async def get_note(Note: NotesRepository, note_id: UUID):
    return await Note.get_note(note_id)

@note_router.get(
    "/get_notes/{user_id}",
    response_model=List[NoteResponseSchema],
    summary="Get all the notes for a given user ID."
)
async def get_notes(Note: NotesRepository, user_id: UUID):
    return await Note.get_notes(user_id)

@note_router.patch(
    "/{note_id}",
    response_model=NoteResponseSchema,
    summary="Edit a note."
)
async def patch_note(Note: NotesRepository, data: NotePatchSchema):
    return await Note.update_note(data)

@note_router.delete(
    "/{note_id}",
    response_model=NoteResponseSchema,
    summary="Delete a note with a given ID."
)
async def delete_note(Note: NotesRepository, note_id: UUID):
    deleted_note = await Note.delete_note(note_id)
    
    if deleted_note:
        return JSONResponse(
            content={
                "message": "Note has been deleted successfuly!",
                "deleted_note": {
                    "note_id": str(note_id),
                    "note_text": deleted_note.note_text
                }
            },
            status_code=status.HTTP_200_OK
        )
    
    else:
        return JSONResponse(
            content={
                "message": "There is no such note with a given ID.",
                "given_id": str(note_id)
            },
            status_code=status.HTTP_404_NOT_FOUND
        )
