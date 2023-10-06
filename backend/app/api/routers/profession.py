from fastapi import APIRouter

from app.api.schemas.profession import ProfessionSchema
from app.services.repository import ProfessionsRepository

profession_router = APIRouter(prefix="/professions", tags=["Professions"])


@profession_router.get("/", response_model=list[ProfessionSchema])
async def get_all_professions(
    Profession: ProfessionsRepository,
    limit: int = 10,
):
    return await Profession.get_all_professions(limit)


@profession_router.post("/", response_model=ProfessionSchema)
async def post_profession(
    profession: ProfessionSchema,
    Profession: ProfessionsRepository
):
    return await Profession.create_one(profession)
