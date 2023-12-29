from dataclasses import dataclass, field
from typing import Dict, Optional, TypeVar
from httpx import Headers

from servicenow._internal._request_configuration import RequestConfiguration

from servicenow.table_api._table_entry import TableEntry
from servicenow.table_api._table_item_response import TableItemResponse
from servicenow.table_api._query_params_table_request_builder_post import (
    TableRequestBuilderPostQueryParameters
)


_E = TypeVar("_E", bound=TableEntry)


@dataclass
class TableCollectionPostRequestConfigurations[_E](RequestConfiguration):
    headers: Optional[Headers] = None
    query: TableRequestBuilderPostQueryParameters = None
    mapping: Optional[Dict[str, str]] = None
    response: TableItemResponse[_E] = field(
        default_factory=TableItemResponse[_E]
    )
