from fastapi import APIRouter

from app.api.schemas.user import UserCreateSchema, UserResponseSchema
from app.db.models.user import User

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.get("/", response_model=list[UserResponseSchema])
async def get_users():
    # get all users
    users = await User.all().to_list()

    return users


@user_router.post("/", response_model=UserResponseSchema)
async def create_user(user: UserCreateSchema):
    # create new user
    new_user = User(**user.model_dump())

    # save in database
    await new_user.create()

    return new_user
