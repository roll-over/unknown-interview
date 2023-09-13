from uuid import UUID

from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

from app.api.schemas.cv import CVRequestSchema, CVResponseSchema
from app.exceptions import UserNotAuthenticated, ForbiddenAction
from app.repository import CVsRepository, UserRepository

cv_router = APIRouter(prefix="/cvs", tags=["CVs"])


@cv_router.post(
    "/",
    response_model=CVResponseSchema,
    summary="Create new CV for user",
)
async def create_cv(
    request: Request,
    data: CVRequestSchema,
    CV: CVsRepository,
    User: UserRepository,
):
    user_data = request.session.get("user")
    if user_data:
        cv_owner = await User.get_user(user_data)

        return await CV.create_one(data, owner_data=cv_owner)

    raise UserNotAuthenticated


@cv_router.get(
    "/random_cv",
    response_model=CVResponseSchema,
    summary="Return random user CV",
)
async def get_random_cv(CV: CVsRepository):
    return await CV.get_random()


@cv_router.get(
    "/{cv_id}",
    response_model=CVResponseSchema,
    summary="Return user CV by ID",
)
async def get_user_cv(cv_id: UUID, CV: CVsRepository):
    return await CV.get_one(cv_id)


@cv_router.patch(
    "/{cv_id}",
    response_model=CVResponseSchema,
    summary="Update user CV by ID",
)
async def update_user_cv(
    request: Request,
    data: CVRequestSchema,
    cv_id: UUID,
    CV: CVsRepository,
    User: UserRepository,
):
    user_data = request.session.get("user")
    if user_data:
        cv_owner = await User.get_user(user_data)
        updated_cv = await CV.update_one(data, cv_id, owner_data=cv_owner)

        if updated_cv:
            return updated_cv

        return ForbiddenAction

    raise UserNotAuthenticated


@cv_router.delete(
    "/{cv_id}",
    summary="Delete user CV by ID",
)
async def delete_user_cv(cv_id: UUID, CV: CVsRepository):
    deleted_cv = await CV.delete_one(cv_id)

    if deleted_cv:
        return JSONResponse(
            content={"message": "User CV deleted successfully"},
            status_code=status.HTTP_200_OK,
        )

    return JSONResponse(
        content={"message": "There is no user CV with such ID"},
        status_code=status.HTTP_404_NOT_FOUND,
    )
