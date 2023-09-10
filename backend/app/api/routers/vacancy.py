from uuid import UUID

from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

from app.api.schemas.vacancy import VacancyRequestSchema, VacancyResponseSchema
from app.exceptions import UserNotAuthenticated
from app.repository import UserRepository, VacanciesRepository

vacancy_router = APIRouter(prefix="/vacancies", tags=["Vacancies"])


@vacancy_router.post(
    "/",
    response_model=VacancyResponseSchema,
    summary="Create new company vacancy",
)
async def create_vacancy(
    request: Request,
    vacancy_data: VacancyRequestSchema,
    Vacancy: VacanciesRepository,
    User: UserRepository,
):
    user_data = request.session.get("user")
    if user_data:
        cv_owner = await User.get_user(user_data)

        return await Vacancy.create_one(vacancy_data, owner_data=cv_owner)

    raise UserNotAuthenticated


@vacancy_router.get(
    "/random_vacancy",
    response_model=VacancyResponseSchema,
    summary="Return random company vacancy",
)
async def get_random_vacancy(Vacancy: VacanciesRepository):
    return await Vacancy.get_random()


@vacancy_router.get(
    "/{vacancy_id}",
    response_model=VacancyResponseSchema,
    summary="Return company vacancy by ID",
)
async def get_company_vacancy(vacancy_id: UUID, Vacancy: VacanciesRepository):
    return await Vacancy.get_one(vacancy_id)


@vacancy_router.delete(
    "/{vacancy_id}",
    summary="Delete company vacancy by ID",
)
async def delete_company_vacancy(vacancy_id: UUID, Vacancy: VacanciesRepository):
    deleted_vacancy = await Vacancy.delete_one(vacancy_id)

    if deleted_vacancy:
        return JSONResponse(
            content={"message": "Company vacancy deleted successfully"},
            status_code=status.HTTP_200_OK,
        )

    return JSONResponse(
        content={"message": "There is no company vacancy with such ID"},
        status_code=status.HTTP_404_NOT_FOUND,
    )
