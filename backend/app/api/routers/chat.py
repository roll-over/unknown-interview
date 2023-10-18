from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Query

from app.api.schemas.chat import (
    ChatMessageRequestSchema,
    ChatMessageResponseSchema,
    ChatResponseSchema,
)
from app.services.repository import ChatMessagesRepository, ChatsRepository

chat_router = APIRouter(prefix="/chats", tags=["Chats"])


@chat_router.get(
    "/",
    response_model=list[ChatResponseSchema],
    summary="Get all chats."
)
async def get_all_chats(Chat: ChatsRepository):
    return await Chat.get_chats()


@chat_router.post(
    "/add_message",
    response_model=ChatMessageResponseSchema,
    summary="Post a new message."
)
async def create_new_chat_message(
    data: ChatMessageRequestSchema, Message: ChatMessagesRepository
):
    return await Message.create_one(data=data)


@chat_router.get(
    "/{chat_id}",
    response_model=list[ChatMessageResponseSchema],
    summary="Get a list of the messages of a given chat id."
)
async def get_chat_messages(
    Message: ChatMessagesRepository, 
    chat_id: UUID, 
    page: Annotated[int, Query(ge=0)] = 0, 
    count: Annotated[int, Query(ge=0)] = 50
):
    return await Message.get_chat_messages(chat_id=chat_id, page=page, count=count)