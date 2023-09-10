from uuid import UUID
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.api.schemas.vacancy_note import (
    VacancyNoteRequestSchema,
    VacancyNoteResponseSchema,
)
from app.api.schemas.base import BaseNoteSchema
from app.repository import VacancyNotesRepository

vacancy_note_router = APIRouter(prefix="/vacancy_note", tags=["Vacancy Notes"])


@vacancy_note_router.post("/", response_model=BaseNoteSchema)
async def add_new_note(data: VacancyNoteRequestSchema, Vacancy: VacancyNotesRepository):
    return await Vacancy.add_note(data)


@vacancy_note_router.get("/{vacancy_id}/", response_model=VacancyNoteResponseSchema)
async def get_vacancy_notes(vacancy_id: UUID, Vacancy: VacancyNotesRepository):
    return await Vacancy.get_notes(vacancy_id)


@vacancy_note_router.delete("/{vacancy_id}/", response_class=JSONResponse)
async def delete_vacancy_notes(vacancy_id: UUID, Vacancy: VacancyNotesRepository):
    deleted_notes = await Vacancy.delete_notes(vacancy_id)

    if deleted_notes:
        return JSONResponse(
            content={"message": "Notes for this vacancy deleted successfully"},
            status_code=status.HTTP_200_OK,
        )

    return JSONResponse(
        content={"message": "There is no vacancy or notes for vacancy with such ID"},
        status_code=status.HTTP_404_NOT_FOUND,
    )
