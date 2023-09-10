from beanie import Document
from pydantic import Field


class Skill(Document):
    name: str = Field(..., max_length=20)

    class Settings:
        name = "skills"  # collection name
