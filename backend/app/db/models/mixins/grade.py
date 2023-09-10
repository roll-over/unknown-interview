from enum import Enum


class Grade(str, Enum):
    junior = "junior"
    middle = "middle"
    senior = "senior"
    lead = "lead"
    principal = "principal"

    @classmethod
    def __iter__(cls):
        return iter(cls._member_names_)
