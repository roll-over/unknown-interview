from typing import Union
from uuid import UUID

from pydantic import Field

from .mixins import MatchRelation, UUIDMixin


class Match(UUIDMixin):
    cv_id: UUID
    applicant_relation: MatchRelation = MatchRelation.not_shown
    vacancy_id: UUID
    employer_relation: MatchRelation = MatchRelation.not_shown
    chat_id: Union[UUID | None] = Field(default=None)

    class Settings:
        name = "matches"
