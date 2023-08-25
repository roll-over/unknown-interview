from uuid import UUID

from pydantic import BaseModel


class CvCreateResponseSchema(BaseModel):
    id: UUID
    title: str
    owner_id: UUID
