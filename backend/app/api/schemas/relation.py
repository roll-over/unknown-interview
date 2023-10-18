from uuid import UUID

from pydantic import BaseModel

from app.db.models import MatchRelation


class RelationSchema(BaseModel):
    cv_id: UUID
    vacancy_id: UUID
    relation: MatchRelation
