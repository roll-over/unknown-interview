from fastapi import APIRouter

from app.api.schemas.user import CreateUserResponseSchema, CreateUserRequestSchema
from app.db.models.user import User

user_router = APIRouter(prefix='/users', tags=['Users'])


@user_router.post('/', response_model=CreateUserResponseSchema)
async def create_user(user: CreateUserRequestSchema):
    user_obj = User(**user.model_dump())
    user_obj.save()
    user_obj.id = str(user_obj.id)

    return user_obj
