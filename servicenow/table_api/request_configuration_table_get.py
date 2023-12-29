from dataclasses import dataclass
from typing import Any, Dict, Optional, TypeVar
from httpx import Headers

from servicenow._internal._request_configuration import RequestConfiguration

from servicenow.table_api._table_entry import TableEntry
from servicenow.table_api._table_collection_response import (
    TableCollectionResponse
)
from servicenow.table_api._query_params_table_request_builder_get import (
    TableRequestBuilderGetQueryParameters
)


_E = TypeVar("_E", bound=TableEntry)


@dataclass
class TableCollectionGetRequestConfigurations[_E](RequestConfiguration):
    headers: Optional[Headers] = None
    query: TableRequestBuilderGetQueryParameters = None
    data: Any = None
    mapping: Optional[Dict[str, str]] = None
    response: TableCollectionResponse[_E] = None
