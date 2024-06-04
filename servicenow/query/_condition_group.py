from __future__ import annotations
from typing import List, Optional

from servicenow.query._condition import Condition


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
    def next(self, group: Optional[ConditionGroup] = None) -> None:
        if not isinstance(group, Optional[ConditionGroup]):
            raise TypeError(f"next is not {Optional[ConditionGroup]}")

        self._next = group

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
