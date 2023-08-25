from uuid import UUID

from pydantic import BaseModel

from app.db.engine import database

cv_collection = database['cv']  # create cv collection (table)


# fields that must be in the cv collection
class CvModel(BaseModel):
    id: UUID = None
    title: str
    owner_id: UUID = None
