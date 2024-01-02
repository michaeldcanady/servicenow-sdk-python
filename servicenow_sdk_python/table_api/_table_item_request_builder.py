from typing import Dict, Generic, Optional, Type, TypeVar
from servicenow_sdk_python._internal._client import IClient
from servicenow_sdk_python._internal._request_builder import RequestBuilder
from servicenow_sdk_python._internal._query_parameter import QueryParameter

from servicenow_sdk_python.table_api._table_entry import TableEntry
from servicenow_sdk_python.table_api._table_item_response import TableItemResponse
from servicenow_sdk_python.table_api.request_configuration_table_item_get import (
    TableItemGetRequestConfigurations,
)
from servicenow_sdk_python.table_api.request_configuration_table_item_put import (
    TableItemPutRequestConfigurations,
)

_E = TypeVar("_E", bound=TableEntry)


class TableItemRequestBuilder(RequestBuilder[_E], Generic[_E]):
    def __init__(
        self,
        path_parameters: Dict[str, str],
        client: IClient,
    ) -> None:
        if not path_parameters.get("sysid", None) or not path_parameters.get(
            "table", None
        ):
            raise ValueError("path_parameters needs 'table'")

        super().__init__(
            path_parameters,
            client,
            (
                "{+baseurl}/now/table{/table}{/sysid}{?sysparm_display_value,"
                "sysparm_exclude_reference_link,sysparm_fields,"
                "sysparm_query_no_domain,sysparm_view,sysparm_limit,"
                "sysparm_no_count,,sysparm_offset,sysparm_query,"
                "sysparm_query_category,sysparm_suppress_pagination_header}"
            ),
        )

    def get(
        self,
        response_type: Type[TableItemResponse[_E]],
        query: Optional[QueryParameter] = None,
    ) -> TableItemResponse[_E]:
        if not issubclass(response_type, TableItemResponse):
            raise TypeError(
                (
                    "response_type must be subclass of "
                    f"'{TableItemResponse[_E]}'"
                )
            )

        config = TableItemGetRequestConfigurations[_E](
            query=query,
            response=response_type(),
        )

        return self.send_get(config)

    def put(
        self,
        data: _E,
        response_type: Type[TableItemResponse[_E]],
        query: Optional[QueryParameter] = None,
    ) -> TableItemResponse[_E]:
        if not issubclass(response_type, TableItemResponse):
            raise TypeError(
                (
                    "response_type must be subclass of "
                    f"'{TableItemResponse[_E]}'"
                )
            )

        config = TableItemPutRequestConfigurations[_E](
            query=query,
            data=data,
            response=response_type(),
        )

        return self.send_put(config)
