from __future__ import annotations
from enum import IntEnum, auto


class Comparison(IntEnum):

    NULL = auto()
    EQUALS = auto()
    NOT_EQUALS = auto()
    IN = auto()
    NOT_IN = auto()
    LIKE = auto()
    NOT_LIKE = auto()
    STARTS_WITH = auto()
    ENDS_WITH = auto()
    LESSER_OR_EQUAL = auto()
    GREATER_OR_EQUAL = auto()
    IS_EMPTY = auto()
    IS_NOT_EMPTY = auto()
    IS_ANYTHING = auto()
    BETWEEN = auto()
    IS_SAME = auto()
    IS_DIFFERENT = auto()

    def __str__(self) -> str:
        return {
            Comparison.NULL: "",
            Comparison.EQUALS: "=",
            Comparison.NOT_EQUALS: "!=",
            Comparison.IN: "IN",
            Comparison.NOT_IN: "NOT IN",
            Comparison.LIKE: "LIKE",
            Comparison.NOT_LIKE: "NOT LIKE",
            Comparison.STARTS_WITH: "STARTSWITH",
            Comparison.ENDS_WITH: "ENDSWITH",
            Comparison.LESSER_OR_EQUAL: "<=",
            Comparison.GREATER_OR_EQUAL: ">=",
            Comparison.IS_EMPTY: "ISEMPTY",
            Comparison.IS_NOT_EMPTY: "ISNOTEMPTY",
            Comparison.IS_ANYTHING: "ANYTHING",
            Comparison.BETWEEN: "BETWEEN",
            Comparison.IS_SAME: "SAMEAS",
            Comparison.IS_DIFFERENT: "NSAMEAS",
        }[self]
