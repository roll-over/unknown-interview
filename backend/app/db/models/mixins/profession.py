from enum import Enum


class Profession(str, Enum):
    developer = "разработчик"
    designer = "дизайнер"
    manager = "менеджер"

    @classmethod
    def __iter__(cls):
        return iter(cls._member_names_)
