from fastapi import APIRouter

from app.api.schemas.user import UserCreateResponseSchema, UserCreateRequestSchema
from app.models.user import User

user_router = APIRouter(prefix='/users', tags=['Users'])


@user_router.post('/', response_model=UserCreateResponseSchema)
async def create_user(user: UserCreateRequestSchema):
    # create new user
    new_user = User(**user.model_dump())

    # save in database
    await new_user.create()

    return new_user
