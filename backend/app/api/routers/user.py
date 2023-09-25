from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from app.api.schemas.user import (
    UserDataListResponseSchema,
    UserEmailSchema,
    UserRequestSchema,
    UserResponseSchema,
)
from app.repository import UserRepository
from app.utils import current_user

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.get("/", response_model=list[UserResponseSchema])
async def get_users(User: UserRepository):
    return await User.get_all_users()


@user_router.post("/", response_model=UserResponseSchema)
async def create_user(data: UserRequestSchema, User: UserRepository):
    return await User.create_one(data)


@user_router.delete(
    "/{user_email}",
    summary="Delete user by email",
)
async def delete_user(user_email: UserEmailSchema, User: UserRepository):
    deleted_user = await User.delete_user(user_email)

    if deleted_user:
        return JSONResponse(
            content={"message": "User deleted successfully"},
            status_code=status.HTTP_200_OK,
        )

    return JSONResponse(
        content={"message": "There is no user with such email"},
        status_code=status.HTTP_404_NOT_FOUND,
    )


@user_router.get("/records", response_model=UserDataListResponseSchema)
async def get_user_job_data(
        User: UserRepository,
        owner: UserResponseSchema = Depends(current_user),
):
    return await User.get_cv_vacancy_data(owner)
