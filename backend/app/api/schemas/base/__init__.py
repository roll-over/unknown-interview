from app.db.models.mixins import Role as UserRole

from .cv_vacancy import ErrorSchema, RequestBaseSchema, ResponseBaseSchema
from .note import BaseNoteSchema, NoteRequestSchema, NoteResponseSchema

__all__ = (
    "RequestBaseSchema",
    "ResponseBaseSchema",
    "NoteResponseSchema",
    "NoteRequestSchema",
    "BaseNoteSchema",
    'ErrorSchema',
    'UserRole',
)
