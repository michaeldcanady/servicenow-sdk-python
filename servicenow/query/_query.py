from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

@dataclass
class Query:
    first: Optional[ConditionGroup] = None
    last: Optional[ConditionGroup] = None

    def add_group(self, group: ConditionGroup) -> Query:

        if not isinstance(group, ConditionGroup):
            raise TypeError(f"condition is not {ConditionGroup}")

        if self.first is None:
            self.first = group
        if self.last is not None:
            self.last.next = group
        else:
            self.first.next = group
        self.last = group
        return self

    def __str__(self) -> str:
        query_str = ''
        current_group = self.first
        while current_group is not None:
            query_str += str(current_group)
            current_group = current_group.next
            if current_group is not None:
                query_str += str(Logical.AND)
        return query_str
