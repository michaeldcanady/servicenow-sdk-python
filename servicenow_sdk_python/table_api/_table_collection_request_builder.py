from typing import Dict, Generic, Optional, Type, TypeVar
from servicenow_sdk_python._internal._client import IClient
from servicenow_sdk_python._internal._request_builder import RequestBuilder

from servicenow_sdk_python.table_api._table_entry import TableEntry
from servicenow_sdk_python.table_api._table_collection_response import (
    TableCollectionResponse
)
from servicenow_sdk_python.table_api._table_item_response import (
    TableItemResponse
)
from servicenow_sdk_python.table_api.request_configuration_table_get import (
    TableCollectionGetRequestConfigurations
)
from servicenow_sdk_python.table_api._table_post_request_configuration import (
    TableCollectionPostRequestConfigurations
)
from servicenow_sdk_python.table_api._query_params_table_request_builder_get import (
    TableRequestBuilderGetQueryParameters,
)
from servicenow_sdk_python.table_api._query_params_table_request_builder_post import (
    TableRequestBuilderPostQueryParameters,
)

_E = TypeVar("_E", bound=TableEntry)


class TableCollectionRequestBuilder(RequestBuilder, Generic[_E]):
    """A class used to build the request for a table collection."""

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
                "sysparm_no_count,sysparm_offset,sysparm_query,"
                "sysparm_query_category,sysparm_suppress_pagination_header}"
            ),
        )

    def get(
        self,
        response_type: Type[TableCollectionResponse[_E]],
        query: Optional[TableRequestBuilderGetQueryParameters] = None,
    ) -> TableCollectionResponse[_E]:
        """
        Sends a GET request.

        Args:
            response_type (Type[TableCollectionResponse[_E]]):
            The type of the response.
            query (Optional[TableRequestBuilderGetQueryParameters]):
            The query of the request.

        Returns:
            TableCollectionResponse[_E]: The response of the GET request.

        Raises:
            TypeError:
            If response_type is not a subclass of `TableCollectionResponse`.
            If query is not an instance of
            `Optional[TableRequestBuilderGetQueryParameters]`
        """

        if not issubclass(response_type, TableCollectionResponse):
            raise TypeError(
                (
                    "response_type must be subclass of "
                    f"'{TableCollectionResponse[_E]}'"
                )
            )

        if not isinstance(
            query, Optional[TableRequestBuilderGetQueryParameters]
        ):
            raise TypeError(
                (
                    "query must be instance of "
                    f"'{Optional[TableRequestBuilderGetQueryParameters]}'"
                )
            )

        config = TableCollectionGetRequestConfigurations[TableEntry](
            query=query,
            response=response_type(),
        )

        return self.send_get(config)

    def post(
        self,
        entry: _E,
        response_type: Type[TableItemResponse[_E]],
        query: Optional[TableRequestBuilderPostQueryParameters] = None,
    ) -> TableItemResponse[_E]:
        """
        Sends a POST request.

        Args:
            entry (_E): The entry of the table.
            response_type (Type[TableItemResponse[_E]]):
            The type of the response.
            query (Optional[TableRequestBuilderPostQueryParameters]):
            The query of the request.

        Returns:
            TableEntry: The entry of the table.

        Raises:
            TypeError:
            If response_type is not a subclass of `TableItemResponse`.
            If query is not an instance of
            `Optional[TableRequestBuilderPostQueryParameters]`
        """

        if not issubclass(response_type, TableItemResponse):
            raise TypeError(
                (
                    "response_type must be subclass of "
                    f"'{TableItemResponse[_E]}'"
                )
            )

        if not isinstance(
            query, Optional[TableRequestBuilderPostQueryParameters]
        ):
            raise TypeError(
                (
                    "query must be instance of "
                    f"'{Optional[TableRequestBuilderPostQueryParameters]}'"
                )
            )

        config = TableCollectionPostRequestConfigurations(
            query=query,
            data=entry,
            response=response_type(),
        )

        return self.send_post(config)
