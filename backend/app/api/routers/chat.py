from typing import Annotated, List
from uuid import UUID

from fastapi import APIRouter, Depends, Query

from app.api.schemas.chat import (
    ChatResponseSchema,
    ChatsResponseSchema,
    MessageRequestSchema,
    MessageResponseSchema,
)
from app.api.schemas.user import UserResponseSchema
from app.services.unitorwork import Chat_dep
from app.utils import current_user

chat_router = APIRouter(prefix="/chats", tags=["Chats"])


@chat_router.get(
    "/",
    response_model=List[ChatsResponseSchema],
    summary="Get all chats that are related to a given vacancy/cv id."
)
async def get_all_chats(
        Chat: Chat_dep,
        record_id: UUID,
        user: UserResponseSchema = Depends(current_user),
):
    return await Chat.fetch_related_chats(record_id=record_id, current_user=user)


@chat_router.post(
    "/add_message",
    response_model=MessageResponseSchema,
    summary="Post a new message."
)
async def create_new_chat_message(
        data: MessageRequestSchema,
        Message: Chat_dep,
        author: UserResponseSchema = Depends(current_user),
):
    return await Message.create_message(data=data, author=author)


@chat_router.get(
    "/{chat_id}",
    response_model=ChatResponseSchema,
    summary="Get chat with messages and notes."
)
async def get_chat_data(
        Message: Chat_dep,
        chat_id: UUID,
        user: UserResponseSchema = Depends(current_user),
        page: Annotated[int, Query(ge=0)] = 0,
        count: Annotated[int, Query(ge=0)] = 50,
):
    return await Message.fetch_chat(
        chat_id=chat_id,
        current_user=user,
        page=page,
        count=count,
    )
