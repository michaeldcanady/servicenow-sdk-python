from typing import Generic, TypeVar
from httpx import Headers

from pydantic import BaseModel

from servicenow_sdk_python.table_api._table_entry import TableEntry

_E = TypeVar("_E", bound=TableEntry)


class TableItemResponse(BaseModel, Generic[_E]):
    result: _E = None

    def parse_headers(self, headers: Headers) -> None:
        pass
