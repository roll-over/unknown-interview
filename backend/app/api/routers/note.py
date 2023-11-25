from uuid import UUID

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from app.api.schemas.note import NotePatchSchema, NoteRequestSchema, NoteResponseSchema
from app.api.schemas.user import UserResponseSchema
from app.services import Chats as Note_dep
from app.utils import current_user

note_router = APIRouter(prefix="/notes", tags=["Notes"])


@note_router.post(
    "/add_note",
    response_model=NoteResponseSchema,
    summary="Post a new note."
)
async def add_note(
    Note: Note_dep,
    data: NoteRequestSchema,
    user: UserResponseSchema = Depends(current_user),
):
    return await Note.add_note(data=data, author=user)


@note_router.get(
    "/{note_id}",
    response_model=NoteResponseSchema,
    summary="Get a note by ID."
)
async def get_note(
    Note: Note_dep,
    note_id: UUID,
    user: UserResponseSchema = Depends(current_user),
):
    return await Note.get_note(note_id=note_id, author=user)


@note_router.patch(
    "/{note_id}",
    response_model=NoteResponseSchema,
    summary="Edit a note."
)
async def patch_note(
    note_id: UUID,
    Note: Note_dep,
    data: NotePatchSchema,
    user: UserResponseSchema = Depends(current_user),
):
    return await Note.update_note(data, note_id=note_id, author=user)


@note_router.delete(
    "/{note_id}",
    response_model=NoteResponseSchema,
    summary="Delete a note with a given ID."
)
async def delete_note(
    Note: Note_dep,
    note_id: UUID,
    user: UserResponseSchema = Depends(current_user),
):
    deleted_note = await Note.delete_note(note_id=note_id, author=user)

    if deleted_note:
        return JSONResponse(
            content={
                "message": "Note deleted successfully."
            },
            status_code=status.HTTP_200_OK
        )

    else:
        return JSONResponse(
            content={
                "message": "There is no such note with a given ID.",
            },
            status_code=status.HTTP_404_NOT_FOUND
        )
