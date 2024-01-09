from __future__ import annotations
from dataclasses import dataclass
from enum import IntEnum, auto
from typing import Any, List, Optional


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


class Condition:

    def __init__(self, field: str, operator: Comparison, value: Any) -> None:
        self._field = field
        self._operator = operator
        self._value = value

    def __str__(self) -> str:

        condition_str = f"{self._field}{self._operator}"
        if self._value is not None:
            value_str = self._value
            if isinstance(self._value, list):
                value_str = ",".join(self._value)
            condition_str += value_str
        return condition_str


class ConditionGroup:

    _next: Optional[ConditionGroup]

    def __init__(self, operator, conditions: List[Condition] = None) -> None:
        self._operator = operator
        self._conditions = conditions or []
        self._next = None

    def add_condition(self, condition: Condition) -> None:
        """_summary_

        Args:
            condition (Condition): _description_

        Raises:
            TypeError: _description_

        Returns:
            _type_: _description_
        """
        if not isinstance(condition, Condition):
            raise TypeError(f"condition is not {Condition}")
        self._conditions.append(condition)

    @property
    def next(self) -> Optional[ConditionGroup]:
        return self._next

    @next.setter
    def next(self, next: Optional[ConditionGroup] = None) -> None:
        if not isinstance(next, Optional[ConditionGroup]):
            raise TypeError(f"next is not {Optional[ConditionGroup]}")
        
        self._next = next

    def __str__(self) -> str:
        """_summary_

        Raises:
            TypeError: _description_

        Returns:
            str: _description_
        """

        return f'{self._operator}'.join(
            [str(condition) for condition in self._conditions]
        )


class OrConditionGroup(ConditionGroup):
    def __init__(self, conditions: List[Condition]) -> None:
        super().__init__(Logical.OR, conditions)


class AndConditionGroup(ConditionGroup):
    def __init__(self, conditions: List[Condition]) -> None:
        super().__init__(Logical.AND, conditions)


@dataclass
class Query:
    first: Optional[ConditionGroup] = None
    last: Optional[ConditionGroup] = None

    def __str__(self) -> str:
        query_str = ''
        current_group = self.first
        while current_group is not None:
            query_str += str(current_group)
            current_group = current_group.next
            if current_group is not None:
                query_str += str(Logical.AND)
        return query_str
