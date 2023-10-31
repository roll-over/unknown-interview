from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Query

from app.api.schemas.chat import (
    ChatMessageRequestSchema,
    ChatMessageResponseSchema,
    ChatResponseSchema,
)
from app.services.unitorwork import Chat_dep

chat_router = APIRouter(prefix="/chats", tags=["Chats"])


@chat_router.get(
    "/",
    response_model=list[ChatResponseSchema],
    summary="Get all chats that are related to a given vacancy/cv id."
)
async def get_all_chats(Chat: Chat_dep, vacancy_or_cv_id: UUID):
    return await Chat.get_many_chats(vacancy_or_cv_id)


@chat_router.post(
    "/add_message",
    response_model=ChatMessageResponseSchema,
    summary="Post a new message."
)
async def create_new_chat_message(
    request_body: ChatMessageRequestSchema, Message: Chat_dep
):
    return await Message.create_message(request_body)


@chat_router.get(
    "/{chat_id}",
    response_model=list[ChatMessageResponseSchema],
    summary="Get a sorted list of the messages of a chat."
)
async def get_messages(
    Message: Chat_dep, 
    chat_id: UUID, 
    page: Annotated[int, Query(ge=0)] = 0, 
    count: Annotated[int, Query(ge=0)] = 50
):
    return await Message.get_messages(chat_id=chat_id, page=page, count=count)