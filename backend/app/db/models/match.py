from uuid import UUID

from .mixins import MatchRelation, UUIDMixin


class Match(UUIDMixin):
    cv_id: UUID
    applicant_relation: MatchRelation = MatchRelation.not_shown
    vacancy_id: UUID
    employer_relation: MatchRelation = MatchRelation.not_shown

    class Settings:
        name = "matches"
