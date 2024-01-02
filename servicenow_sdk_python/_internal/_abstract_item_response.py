from typing import Generic, TypeVar

from servicenow_sdk_python._internal._abstract_response import AbstractResponse


_E = TypeVar("_E")


class AbstractItemResponse(AbstractResponse[_E], Generic[_E]):
    pass
