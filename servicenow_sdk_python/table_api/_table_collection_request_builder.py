from typing import Dict, Generic, Optional, Type, TypeVar
from servicenow_sdk_python._internal._client import IClient
from servicenow_sdk_python._internal._request_builder import RequestBuilder
from servicenow_sdk_python._internal._query_parameter import QueryParameter

from servicenow_sdk_python.table_api._table_entry import TableEntry
from servicenow_sdk_python.table_api._table_collection_response import (
    TableCollectionResponse
)
from servicenow_sdk_python.table_api.request_configuration_table_get import (
    TableCollectionGetRequestConfigurations
)
from servicenow_sdk_python.table_api._table_post_request_configuration import (
    TableCollectionPostRequestConfigurations
)

_E = TypeVar("_E", bound=TableEntry)


class TableCollectionRequestBuilder(RequestBuilder, Generic[_E]):

    def __init__(
        self,
        path_parameters: Dict[str, str],
        client: IClient,
    ) -> None:

        if not path_parameters.get("table", None):
            raise ValueError("path_parameters needs 'table'")

        super().__init__(
            path_parameters,
            client,
            (
                "{+baseurl}/now/table{/table}{?sysparm_display_value,"
                "sysparm_exclude_reference_link,sysparm_fields,"
                "sysparm_query_no_domain,sysparm_view,sysparm_limit,"
                "sysparm_no_count,,sysparm_offset,sysparm_query,"
                "sysparm_query_category,sysparm_suppress_pagination_header}"
            ),
        )

    def get(
        self,
        response_type: Type[TableCollectionResponse[_E]],
        query: Optional[QueryParameter] = None,
    ) -> TableCollectionResponse[_E]:

        if not issubclass(response_type, TableCollectionResponse):
            raise TypeError(
                (
                    "response_type must be subclass of "
                    f"'{TableCollectionResponse[_E]}'"
                )
            )

        config = TableCollectionGetRequestConfigurations[TableEntry](
            query=query,
            response=response_type(),
        )

        return self.send_get(config)

    def post(
        self,
        entry: TableEntry,
        response_type: Type[TableCollectionResponse[_E]],
        query: Optional[QueryParameter] = None,
    ) -> TableEntry:

        config = TableCollectionPostRequestConfigurations(
            query=query,
            data=entry,
            response=response_type(),
        )

        return self.send_post(entry, config)
