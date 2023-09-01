from uuid import UUID
from fastapi import APIRouter

from app.api.schemas.cv import CVRequestSchema, CVResponseSchema
from app.models.cv import CV

cv_router = APIRouter(prefix="/cv", tags=["CV"])


@cv_router.post(
    "/",
    response_model=CVResponseSchema,
    summary="Create new CV for user",
)
async def create_cv(user_cv: CVRequestSchema):
    new_user_cv = CV(**user_cv.model_dump())
    await new_user_cv.create()

    return new_user_cv


@cv_router.get(
    "/random_cv",
    response_model=CVResponseSchema,
    summary="Return random user CV",
)
async def get_random_cv():
    random_user_cv = await CV.aggregate([{"$sample": {"size": 1}}]).to_list(1)

    if random_user_cv:
        return random_user_cv[0]


@cv_router.get(
    "/{cv_id}",
    response_model=CVResponseSchema,
    summary="Return user CV by ID",
)
async def get_user_cv(cv_id: UUID):
    user_cv = await CV.find_one({"custom_id": cv_id})

    return user_cv


@cv_router.get(
    "/delete/{cv_id}",
    summary="Delete user CV by ID",
)
async def delete_user_cv(cv_id: UUID):
    user_cv = await CV.find_one({"custom_id": cv_id})
    if user_cv:
        await user_cv.delete()

        return {"message": "User CV deleted successfully"}

    return {"error": "There is no user CV with such ID"}
