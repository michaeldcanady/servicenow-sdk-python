

from enum import IntEnum, auto


class View(IntEnum):

    NONE = 0
    DESKTOP = auto()
    MOBILE = auto()
    BOTH = auto()

    def __str__(self) -> str:

        return [
            "",
            "desktop",
            "mobile",
            "both",
        ][self]
