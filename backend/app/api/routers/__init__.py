from fastapi import APIRouter

from .auth import auth_router
from .cv import cv_router
from .user import user_router
from .vacancy import vacancy_router
from .cv_note import cv_note_router
from .vacancy_note import vacancy_note_router
from .collection import collection_router


v1 = APIRouter(prefix="/api/v1")

v1.include_router(auth_router)
v1.include_router(user_router)
v1.include_router(cv_router)
v1.include_router(cv_note_router)
v1.include_router(vacancy_router)
v1.include_router(vacancy_note_router)
v1.include_router(collection_router)

__all__ = ("v1",)
