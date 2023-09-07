from fastapi import APIRouter
from app.db.models.mixins import Grade, Title, Profession


collection_router = APIRouter(prefix="/collections", tags=["Collections"])


@collection_router.get(
    "/grade", summary="Return the collection of existing grades in DB"
)
async def get_grades(limit: int = 10):
    return list(Grade)[:limit]


@collection_router.get(
    "/title", summary="Return the collection of existing title in DB"
)
async def get_titles(limit: int = 10):
    return list(Title)[:limit]


@collection_router.get("/profession", summary="Return the collection of existing professions in DB")
async def get_professions(limit: int = 10):
    return list(Profession)[:limit]
