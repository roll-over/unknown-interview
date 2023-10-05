from typing import Annotated

from fastapi import Depends

from .interfaces import AbstractRecordHandler
from .record_handler import RecordHandler

Records = Annotated[AbstractRecordHandler, Depends(RecordHandler)]
