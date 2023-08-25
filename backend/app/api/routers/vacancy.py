import uuid

from fastapi import APIRouter

from app.api.schemas.vacancy import VacancyCreateResponseSchema
from app.models.vacancy import vacancies_collection, VacancyModel

vacancy_router = APIRouter(prefix='/vacancies', tags=['Vacancies'])


@vacancy_router.post('/', response_model=VacancyCreateResponseSchema)
async def create_vacancy(vacancy: VacancyModel):
    vacancy.id = str(uuid.uuid4())
    vacancy.owner_id = str(uuid.uuid4())  # must be the current user id from request

    # insert a vacancy into the cv collection
    result = await vacancies_collection.insert_one(vacancy.model_dump())

    # get the created vacancy
    created_vacancy = await vacancies_collection.find_one({'_id': result.inserted_id})

    return created_vacancy
