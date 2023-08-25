import uuid

from fastapi import APIRouter

from app.api.schemas.user import UserCreateResponseSchema
from app.models.user import UserModel, users

user_router = APIRouter(prefix='/users', tags=['Users'])


@user_router.post('/', response_model=UserCreateResponseSchema)
async def create_user(user: UserModel):
    user.id = str(uuid.uuid4())

    # insert a user into the users collection
    result = await users.insert_one(user.model_dump())

    # get the created user
    created_user = await users.find_one({"_id": result.inserted_id})

    return created_user
