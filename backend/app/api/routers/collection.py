from fastapi import APIRouter
from app.db.models.mixins import Grade, Title
from typing import List

collection_router = APIRouter(prefix="/collections", tags=["Collections"])


@collection_router.get(
    "/grade",
    response_model=List[Grade],
    summary="Return the collection of existing grades in DB",
)
async def get_grades(limit: int = 10):
    return list(Grade)[:limit]


@collection_router.get(
    "/title",
    response_model=List[Title],
    summary="Return the collection of existing title in DB",
)
async def get_grades(limit: int = 10):
    return list(Title)[:limit]
