from dataclasses import dataclass
from typing import Any, Dict, Generic, Optional, TypeVar
from httpx import Headers

from servicenow_sdk_python._internal._request_configuration import (
    RequestConfiguration
)

from servicenow_sdk_python.table_api._table_entry import TableEntry
from servicenow_sdk_python.table_api._table_collection_response import (
    TableCollectionResponse
)
from servicenow_sdk_python.table_api._query_params_table_request_builder_get import (
    TableRequestBuilderGetQueryParameters
)


_E = TypeVar("_E", bound=TableEntry)


@dataclass
class TableCollectionGetRequestConfigurations(
    RequestConfiguration,
    Generic[_E],
):
    headers: Optional[Headers] = None
    query: TableRequestBuilderGetQueryParameters = None
    data: Any = None
    mapping: Optional[Dict[str, str]] = None
    response: TableCollectionResponse[_E] = None
