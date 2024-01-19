from dataclasses import dataclass, field
from typing import Dict, Generic, Optional, TypeVar
from httpx import Headers

from servicenow_sdk_python._internal._request_configuration import (
    RequestConfiguration
)

from servicenow_sdk_python.table_api._table_entry import TableEntry
from servicenow_sdk_python.table_api._table_item_response import (
    TableItemResponse
)
from servicenow_sdk_python.table_api._query_params_table_request_builder_post import (
    TableRequestBuilderPostQueryParameters
)


_E = TypeVar("_E", bound=TableEntry)


@dataclass
class TableCollectionPostRequestConfigurations(
    RequestConfiguration,
    Generic[_E]
):
    """A class that represents the configurations for a POST request to a
    table collection.
    """

    headers: Optional[Headers] = None
    """The headers for the POST request."""

    query: TableRequestBuilderPostQueryParameters = None
    """The query parameters for the POST request."""

    mapping: Optional[Dict[str, str]] = None
    """The error mapping for the POST request."""

    response: TableItemResponse[_E] = field(
        default_factory=TableItemResponse[_E]
    )
    """The response from the POST request."""
