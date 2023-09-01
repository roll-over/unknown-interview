from .auth import auth_router
from .cv import cv_router
from .user import user_router
from .vacancy import vacancy_router
from .cv_note import cv_note_router

from fastapi import APIRouter

v1 = APIRouter(prefix="/api/v1")

v1.include_router(user_router)
v1.include_router(cv_router)
v1.include_router(cv_note_router)
v1.include_router(vacancy_router)
v1.include_router(auth_router)

__all__ = ["v1"]
