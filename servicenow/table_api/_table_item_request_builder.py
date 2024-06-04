from typing import Dict, Generic, Optional, Type, TypeVar
from servicenow._internal._client import IClient
from servicenow._internal._request_builder import RequestBuilder

from servicenow.table_api._table_entry import TableEntry
from servicenow.table_api._table_item_response import (
    TableItemResponse
)
from servicenow.table_api._query_params_table_item_request_builder_get import (
    TableItemGetQueryParameters
)
from servicenow.table_api._query_params_table_item_request_builder_put import (
    TableItemPutQueryParameters
)
from servicenow.table_api.request_configuration_table_item_get import (
    TableItemGetRequestConfigurations,
)
from servicenow.table_api.request_configuration_table_item_put import (
    TableItemPutRequestConfigurations,
)

_E = TypeVar("_E", bound=TableEntry)


class TableItemRequestBuilder(RequestBuilder[_E], Generic[_E]):
    """A class that builds requests for table items in the ServiceNow SDK."""

    def __init__(
        self,
        path_parameters: Dict[str, str],
        client: IClient,
    ) -> None:
        if not path_parameters.get("sysid", None) or not path_parameters.get(
            "table", None
        ):
            raise ValueError("path_parameters needs 'table' and 'sysid'")

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
        query: Optional[TableItemGetQueryParameters] = None,
    ) -> TableItemResponse[_E]:
        """
        Sends a GET request.

        Args:
            response_type (Type[TableItemResponse[_E]]):
            The type of the response.
            query (Optional[TableItemGetQueryParameters]):
            The query parameters for the GET request.

        Returns:
            TableItemResponse[_E]: The response from the GET request.

        Raises:
            TypeError:
            If response_type is not a subclass of TableItemResponse
            or if query is not an instance of TableItemGetQueryParameters.
        """

        if not issubclass(response_type, TableItemResponse):
            raise TypeError(
                (
                    "response_type must be subclass of "
                    f"'{TableItemResponse[_E]}'"
                )
            )

        if not isinstance(
            query, Optional[TableItemGetQueryParameters]
        ):
            raise TypeError(
                (
                    "query must be instance of "
                    f"'{Optional[TableItemGetQueryParameters]}'"
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
        query: Optional[TableItemPutQueryParameters] = None,
    ) -> TableItemResponse[_E]:
        """
        Sends a PUT request.

        Args:
            data (_E): The data to be sent in the PUT request.
            response_type (Type[TableItemResponse[_E]]):
            The type of the response.
            query (Optional[TableItemPutQueryParameters]):
            The query parameters for the PUT request.

        Returns:
            TableItemResponse[_E]: The response from the PUT request.

        Raises:
            TypeError: If response_type is not a subclass of TableItemResponse
            or if query is not an instance of TableItemPutQueryParameters.
        """

        if not issubclass(response_type, TableItemResponse):
            raise TypeError(
                (
                    "response_type must be subclass of "
                    f"'{TableItemResponse[_E]}'"
                )
            )

        if not isinstance(
            query, Optional[TableItemPutQueryParameters]
        ):
            raise TypeError(
                (
                    "query must be instance of "
                    f"'{Optional[TableItemPutQueryParameters]}'"
                )
            )

        config = TableItemPutRequestConfigurations[_E](
            query=query,
            data=data,
            response=response_type(),
        )

        return self.send_put(config)
