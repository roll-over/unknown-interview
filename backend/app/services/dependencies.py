from typing import Annotated

from fastapi import Depends

from .chat_handler import ChatHandler
from .interfaces import (
    AbstractChatHandler,
    AbstractRecordHandler,
    AbstractRelationHandler,
)
from .record_handler import RecordHandler
from .relation_handler import RelationHandler

Records = Annotated[AbstractRecordHandler, Depends(RecordHandler)]
Relations = Annotated[AbstractRelationHandler, Depends(RelationHandler)]
Chats = Annotated[AbstractChatHandler, Depends(ChatHandler)]
