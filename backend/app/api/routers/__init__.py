from fastapi import APIRouter

from .auth import auth_router
from .chat import chat_router
from .collection import collection_router
from .cv import cv_router
from .note import note_router
from .profession import profession_router
from .relation import relation_router
from .skill import skill_router
from .user import user_router
from .vacancy import vacancy_router

v1 = APIRouter(prefix="/api/v1")

v1.include_router(auth_router)
v1.include_router(user_router)
v1.include_router(cv_router)
v1.include_router(vacancy_router)
v1.include_router(relation_router)
v1.include_router(chat_router)
v1.include_router(note_router)
v1.include_router(collection_router)
v1.include_router(profession_router)
v1.include_router(skill_router)

__all__ = ("v1",)
