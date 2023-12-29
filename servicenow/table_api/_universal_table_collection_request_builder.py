from typing import Optional
from servicenow.table_api._table_collection_request_builder import (
    TableCollectionRequestBuilder
)

from servicenow.table_api._table_entry import TableEntry
from servicenow.table_api._table_collection_response import (
    TableCollectionResponse
)
from servicenow.table_api._query_params_table_request_builder_get import (
    TableRequestBuilderGetQueryParameters
)


class UniversalTableCollectionRequestBuilder(
    TableCollectionRequestBuilder[TableEntry]
):

    def get(
        self,
        query: Optional[TableRequestBuilderGetQueryParameters] = None,
    ) -> TableCollectionResponse[TableEntry]:

        return super().get(
            query=query,
            response_type=TableCollectionResponse[TableEntry],
        )
