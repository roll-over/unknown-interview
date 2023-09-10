from enum import Enum


class Title(str, Enum):
    member = "member"
    lead = "lead"
    teamlead = "teamlead"
    manager = "manager"
    director = "director"

    @classmethod
    def __iter__(cls):
        return iter(cls._member_names_)
