from typing import TypeVar
from servicenow_sdk_python._internal._page_iterator import AbstractPageIterator
from servicenow_sdk_python._internal._request_information import (
    RequestInformation
)
from servicenow_sdk_python._internal._http_method import HTTPMethod

from servicenow_sdk_python.table_api._table_entry import TableEntry
from servicenow_sdk_python.table_api._table_collection_response import (
    TableCollectionResponse
)

_E = TypeVar("_E", bound=TableEntry)


class TablePageIterator(AbstractPageIterator[_E]):

    def _fetch_page(self, uri: str) -> TableCollectionResponse[_E]:
        """_summary_

        Args:
            uri (str): _description_

        Returns:
            TableItemResponse: _description_
        """

        if uri == "" or uri is None:
            raise Exception("URI can't be empty")

        req_info = RequestInformation()
        req_info.method = HTTPMethod.GET
        req_info.set_uri(uri)

        resp = self.client.send(req_info, None, TableCollectionResponse[_E])

        return resp
