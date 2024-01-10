from __future__ import annotations
from typing import List

from servicenow_sdk_python.query._logical import Logical
from servicenow_sdk_python.query._condition import Condition
from servicenow_sdk_python.query._condition_group import ConditionGroup


class AndConditionGroup(ConditionGroup):
    def __init__(self, conditions: List[Condition]) -> None:
        super().__init__(Logical.AND, conditions)
