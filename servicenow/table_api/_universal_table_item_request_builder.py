from typing import Optional
from servicenow.table_api._table_item_request_builder import (
    TableItemRequestBuilder,
)

from servicenow.table_api._table_entry import TableEntry
from servicenow.table_api._table_item_response import TableItemResponse
from servicenow.table_api._query_params_table_item_request_builder_get import (
    TableItemGetQueryParameters
)


class UniversalTableItemRequestBuilder(
    TableItemRequestBuilder[TableEntry]
):
    def get(
        self,
        query: Optional[TableItemGetQueryParameters] = None,
    ) -> TableItemResponse[TableEntry]:
        response_type = TableItemResponse[TableEntry]

        return super().get(response_type, query)
