from abc import abstractmethod
from typing import TypeVar
from pydantic import BaseModel

from servicenow._internal._page_result import PageResult


_E = TypeVar("_E")


class AbstractResponse[_E](BaseModel):

    @abstractmethod
    def to_page(self) -> PageResult[_E]:
        return NotImplemented
