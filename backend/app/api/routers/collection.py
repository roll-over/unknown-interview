from fastapi import APIRouter
from app.db.models.mixins import Grade

collection_router = APIRouter(prefix="/collections", tags=["Collections"])


@collection_router.get(
    "/grade", summary="Return the collection of existing grades in DB"
)
async def get_grades(limit: int = 10):
    return list(Grade)[:limit]
