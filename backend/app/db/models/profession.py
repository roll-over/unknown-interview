from beanie import Document
from pydantic import Field


class Profession(Document):
    name: str = Field(..., max_length=20)

    class Settings:
        name = "professions"  # collection name
