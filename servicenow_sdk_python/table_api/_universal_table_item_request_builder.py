from typing import Dict, Optional, Union
from servicenow_sdk_python.table_api._table_item_request_builder import (
    TableItemRequestBuilder,
)

from servicenow_sdk_python.table_api._table_entry import TableEntry
from servicenow_sdk_python.table_api._table_item_response import TableItemResponse
from servicenow_sdk_python.table_api._query_params_table_item_request_builder_get import (
    TableItemGetQueryParameters,
)
from servicenow_sdk_python.table_api._query_params_table_item_request_builder_put import (
    TableItemPutQueryParameters,
)


class UniversalTableItemRequestBuilder(TableItemRequestBuilder[TableEntry]):
    def get(
        self,
        query: Optional[TableItemGetQueryParameters] = None,
    ) -> TableItemResponse[TableEntry]:
        response_type = TableItemResponse[TableEntry]

        return super().get(response_type, query)

    def put(
        self,
        data: Union[Dict[str, str], TableEntry],
        query: Optional[TableItemPutQueryParameters] = None,
    ) -> TableItemResponse[TableEntry]:
        response_type = TableItemResponse[TableEntry]

        if not isinstance(data, Union[dict, TableEntry]):
            raise TypeError(
                "data must be of type Dict[str, str] or TableEntry"
            )

        if isinstance(data, dict):
            data = TableEntry.model_validate(data)

        return super().put(data, response_type, query)
