from typing import Annotated

from fastapi import Depends

from .relation_handler import ChatHandler
from .interfaces import AbstractChatHandler, AbstractRecordHandler
from .record_handler import RecordHandler

Records = Annotated[AbstractRecordHandler, Depends(RecordHandler)]
Chats = Annotated[AbstractChatHandler, Depends(ChatHandler)]
