from enum import IntEnum, auto


class DisplayValue(IntEnum):

    NONE = 0
    TRUE = auto()
    FALSE = auto()
    ALL = auto()

    def __str__(self) -> str:

        return [
            "",
            "true",
            "false",
            "all",
        ][self]
