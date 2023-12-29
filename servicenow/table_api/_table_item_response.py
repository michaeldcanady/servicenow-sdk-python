from typing import TypeVar
from httpx import Headers

from pydantic import BaseModel

from servicenow.table_api._table_entry import TableEntry

_E = TypeVar("_E", bound=TableEntry)


class TableItemResponse[_E](BaseModel):
    result: _E = None

    def parse_headers(self, headers: Headers) -> None:
        pass
