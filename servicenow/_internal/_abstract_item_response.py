from typing import Generic, TypeVar

from servicenow._internal._abstract_response import AbstractResponse


_E = TypeVar("_E")


class AbstractItemResponse(AbstractResponse[_E], Generic[_E]):  # pylint:disable=too-few-public-methods
    """The base for Item Response
    """
