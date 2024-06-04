from __future__ import annotations
from enum import IntEnum, auto


class Logical(IntEnum):
    NULL = 0
    OR = auto()
    AND = auto()

    def __str__(self) -> str:
        return {
            Logical.NULL: "",
            Logical.OR: "^OR",
            Logical.AND: "^",
        }[self]
