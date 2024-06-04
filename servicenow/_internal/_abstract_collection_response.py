from abc import abstractmethod, ABC
from typing import Generic, TypeVar

from servicenow._internal._page_result import PageResult
from servicenow._internal._abstract_response import AbstractResponse


_E = TypeVar("_E")


class ICollectionResponse(AbstractResponse[_E], ABC, Generic[_E]):  # pylint:disable=too-few-public-methods
    """The base for Collection Response
    """

    @abstractmethod
    def to_page(self) -> PageResult[_E]:
        """Converts response to page result

        Returns:
            PageResult[_E]: The page result
        """

        return NotImplemented
