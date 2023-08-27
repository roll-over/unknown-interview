from uuid import UUID, uuid4

from beanie import Document
from pydantic import model_validator


class UUIDMixin(Document):
    custom_id: UUID

    @model_validator(mode='before')
    def generate_uuid(cls, values):
        values['custom_id'] = str(uuid4())
        return values
