from typing import Generic, TypeVar
from httpx import Headers

from pydantic import BaseModel

from servicenow_sdk_python.table_api._table_entry import TableEntry

_E = TypeVar("_E", bound=TableEntry)


class TableItemResponse(BaseModel, Generic[_E]):
    """A class that represents the response from a
    table item request in the ServiceNow SDK.
    """

    result: _E = None
    """The result of the table item request."""

    def parse_headers(self, headers: Headers) -> None:
        """
        Parses the headers from the response.

        Args:
            headers (Headers): The headers from the response.
        """
