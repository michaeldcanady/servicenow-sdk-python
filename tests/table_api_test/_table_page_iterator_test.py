from servicenow_sdk_python.table_api._table_page_iterator import TablePageIterator
from servicenow_sdk_python.table_api._table_entry import TableEntry
from servicenow_sdk_python.table_api._table_collection_response import TableCollectionResponse


def example_collection_resp() -> TableCollectionResponse[TableEntry]:

    entries = [
        TableEntry(),
    ]

    return TableCollectionResponse[TableEntry](result=entries)


def table_page_iterator_iterate(
    example_collection_resp: TableCollectionResponse[TableEntry]
) -> None:

    def callback(entry: TableEntry) -> bool:
        return True

    iterator = TablePageIterator[TableEntry](example_collection_resp)

    iterator.iterate(callback)
