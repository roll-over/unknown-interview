from uuid import UUID
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.api.schemas.cv_note import (
    CVNoteRequestSchema,
    CVNoteResponseSchema,
)
from app.api.schemas.base import BaseNoteSchema
from app.repository import CVNotesRepository


cv_note_router = APIRouter(prefix="/cv_note", tags=["CV Notes"])


@cv_note_router.post(
    "/",
    response_model=BaseNoteSchema,
    summary="Add new HR note to the CV",
)
async def add_new_note(data: CVNoteRequestSchema, CV: CVNotesRepository):
    return await CV.add_note(data)


@cv_note_router.get(
    "/{cv_id}",
    response_model=CVNoteResponseSchema,
    summary="Returns all HR notes on the specified CV",
)
async def get_cv_notes(cv_id: UUID, CV: CVNotesRepository):
    return await CV.get_notes(cv_id)


@cv_note_router.delete(
    "/{cv_id}",
    summary="Delete all HR notes to the CV",
)
async def delete_cv_notes(cv_id: UUID, CV: CVNotesRepository):
    deleted_notes = await CV.delete_notes(cv_id)

    if deleted_notes:
        return JSONResponse(
            content={"message": "Notes for this CV deleted successfully"},
            status_code=status.HTTP_200_OK,
        )

    return JSONResponse(
        content={"message": "There is no CV or notes for CV with such ID"},
        status_code=status.HTTP_404_NOT_FOUND,
    )
