from abc import abstractmethod, ABC
from typing import Generic, TypeVar

from servicenow_sdk_python._internal._page_result import PageResult
from servicenow_sdk_python._internal._abstract_response import AbstractResponse


_E = TypeVar("_E")


class ICollectionResponse(AbstractResponse, ABC, Generic[_E]):

    @abstractmethod
    def to_page(self) -> PageResult[_E]:
        return NotImplemented
