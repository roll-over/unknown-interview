import uuid

from fastapi import APIRouter

from app.api.schemas.cv import CvCreateResponseSchema
from app.models.cv import cv_collection, CvModel

cv_router = APIRouter(prefix='/cv', tags=['Cv'])


@cv_router.post('/', response_model=CvCreateResponseSchema)
async def create_cv(cv: CvModel):
    cv.id = str(uuid.uuid4())
    cv.owner_id = str(uuid.uuid4())  # must be the current user id from request

    # insert a cv into the cv collection
    result = await cv_collection.insert_one(cv.model_dump())

    # get the created cv
    created_cv = await cv_collection.find_one({'_id': result.inserted_id})

    return created_cv
