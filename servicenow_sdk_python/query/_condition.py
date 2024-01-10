from __future__ import annotations
from typing import Any

from servicenow_sdk_python.query._comparison import Comparison


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
