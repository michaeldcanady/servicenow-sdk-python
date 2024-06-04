from dataclasses import dataclass
from typing import Dict, Generic, Optional, TypeVar
from httpx import Headers

from servicenow._internal._request_configuration import RequestConfiguration

from servicenow.table_api._table_entry import TableEntry
from servicenow.table_api._table_item_response import (
    TableItemResponse
)
from servicenow.table_api._query_params_table_item_request_builder_put import (
    TableItemPutQueryParameters
)


_E = TypeVar("_E", bound=TableEntry)


@dataclass
class TableItemPutRequestConfigurations(RequestConfiguration, Generic[_E]):
    headers: Optional[Headers] = None
    query: TableItemPutQueryParameters = None
    data: _E
    mapping: Optional[Dict[str, str]] = None
    response: TableItemResponse[_E] = None
