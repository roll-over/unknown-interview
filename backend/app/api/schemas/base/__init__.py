from app.db.models.mixins import Role as UserRole

from .cv_vacancy import RequestBaseSchema, ResponseBaseSchema

__all__ = (
    "RequestBaseSchema",
    "ResponseBaseSchema",
    'UserRole',
)
