from uuid import UUID

from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse

from app.api.schemas.base import UserRole
from app.api.schemas.user import UserResponseSchema
from app.api.schemas.vacancy import VacancyRequestSchema, VacancyResponseSchema
from app.services import Records as VacancyRecords
from app.utils import current_user

vacancy_router = APIRouter(prefix="/vacancies", tags=["Vacancies"])


@vacancy_router.post(
    "/",
    response_model=VacancyResponseSchema,
    summary="Create new company vacancy",
)
async def create_vacancy(
    request: Request,
    vacancy_data: VacancyRequestSchema,
    Vacancy: VacancyRecords,
    vacancy_owner: UserResponseSchema = Depends(current_user),
):
    return await Vacancy.prepare_record(
        vacancy_data,
        owner_data=vacancy_owner,
        role=UserRole.employer,
    )


@vacancy_router.get(
    "/random_vacancy",
    response_model=VacancyResponseSchema,
    summary="Return random company vacancy",
)
async def get_random_vacancy(
        Vacancy: VacancyRecords,
        vacancy_owner: UserResponseSchema = Depends(current_user),
):
    return await Vacancy.get_matched_record(
        owner_data=vacancy_owner,
        role=UserRole.applicant,
    )


@vacancy_router.get(
    "/{vacancy_id}",
    response_model=VacancyResponseSchema,
    summary="Return company vacancy by ID",
)
async def get_company_vacancy(
        vacancy_id: UUID,
        Vacancy: VacancyRecords,
        record_owner: UserResponseSchema = Depends(current_user),
):
    return await Vacancy.get_record(
        record_id=vacancy_id,
        owner_data=record_owner,
        role=UserRole.employer,
    )


@vacancy_router.patch(
    "/{vacancy_id}",
    response_model=VacancyResponseSchema,
    summary="Update company vacancy by ID",
)
async def update_company_vacancy(
    request: Request,
    vacancy_data: VacancyRequestSchema,
    vacancy_id: UUID,
    Vacancy: VacancyRecords,
    vacancy_owner: UserResponseSchema = Depends(current_user),
):
    return await Vacancy.update_record(
        vacancy_data,
        record_id=vacancy_id,
        owner_data=vacancy_owner,
        role=UserRole.employer,
    )


@vacancy_router.delete(
    "/{vacancy_id}",
    summary="Delete company vacancy by ID",
)
async def delete_company_vacancy(
    vacancy_id: UUID,
    Vacancy: VacancyRecords,
    vacancy_owner: UserResponseSchema = Depends(current_user),

):
    deleted_vacancy = await Vacancy.delete_record(
        record_id=vacancy_id,
        owner_data=vacancy_owner,
        role=UserRole.employer,
    )

    if deleted_vacancy:
        return JSONResponse(
            content={"message": "Company vacancy deleted successfully"},
            status_code=status.HTTP_200_OK,
        )
