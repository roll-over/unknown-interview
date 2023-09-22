from enum import Enum


class Role(str, Enum):
    employer = "employer"
    applicant = "applicant"

    @classmethod
    def __iter__(cls):
        return iter(cls._member_names_)
