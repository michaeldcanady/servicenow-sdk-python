from dataclasses import dataclass
from typing import Any, Dict, Optional, TypeVar
from httpx import Headers

from servicenow._internal._request_configuration import RequestConfiguration

from servicenow.table_api._table_entry import TableEntry
from servicenow.table_api._table_item_response import (
    TableItemResponse
)
from servicenow.table_api._query_params_table_item_request_builder_get import (
    TableItemGetQueryParameters
)


_E = TypeVar("_E", bound=TableEntry)


@dataclass
class TableItemGetRequestConfigurations[_E](RequestConfiguration):
    headers: Optional[Headers] = None
    query: TableItemGetQueryParameters = None
    data: Any = None
    mapping: Optional[Dict[str, str]] = None
    response: TableItemResponse[_E] = None
