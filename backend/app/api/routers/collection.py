from fastapi import APIRouter
from app.db.models.mixins import Grade, Profession

collection_router = APIRouter(prefix="/collections", tags=["Collections"])


@collection_router.get(
    "/grade", summary="Return the collection of existing grades in DB"
)
async def get_grades(limit: int = 10):
    return list(Grade)[:limit]


@collection_router.get("/profession", summary="Return the collection of existing professions in DB")
async def get_professions(limit: int = 10):
    return list(Profession)[:limit]
