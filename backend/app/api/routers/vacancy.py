from uuid import UUID

from fastapi import APIRouter

from app.api.schemas.vacancy import VacancyRequestSchema, VacancyResponseSchema
from app.db.models.vacancy import Vacancy


vacancy_router = APIRouter(prefix="/vacancies", tags=["Vacancies"])


@vacancy_router.post(
    "/",
    response_model=VacancyResponseSchema,
    summary="Create new company vacancy",
)
async def create_vacancy(job_vacancy: VacancyRequestSchema):
    new_vacancy = Vacancy(**job_vacancy.model_dump())
    await new_vacancy.create()

    return new_vacancy


@vacancy_router.get(
    "/random_vacancy",
    response_model=VacancyResponseSchema,
    summary="Return random company vacancy",
)
async def get_random_vacancy():
    random_vacancy = await Vacancy.aggregate([{"$sample": {"size": 1}}]).to_list(1)

    if random_vacancy:
        return random_vacancy[0]


@vacancy_router.get(
    "/{vacancy_id}",
    response_model=VacancyResponseSchema,
    summary="Return company vacancy by ID",
)
async def get_company_vacancy(vacancy_id: UUID):
    found_vacancy = await Vacancy.find_one({"custom_id": vacancy_id})

    return found_vacancy


@vacancy_router.delete(
    "/{vacancy_id}",
    summary="Delete company vacancy by ID",
)
async def delete_company_vacancy(vacancy_id: UUID):
    found_vacancy = await Vacancy.find_one({"custom_id": vacancy_id})
    if found_vacancy:
        await found_vacancy.delete()

        return {"message": "Company vacancy deleted successfully"}

    return {"error": "There is no company vacancy with such ID"}
