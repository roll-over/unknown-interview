from uuid import UUID

from .mixins import UUIDMixin


class MatchCollection(UUIDMixin):
    cv_id: UUID
    vacancy_id: UUID

    class Settings:
        name = 'matches'
