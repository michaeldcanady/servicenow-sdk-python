from typing import Generic, Optional, TypeVar
from servicenow._internal._page_iterator import AbstractPageIterator
from servicenow._internal._request_information import (
    RequestInformation
)
from servicenow._internal._http_method import HTTPMethod

from servicenow.table_api._table_entry import TableEntry
from servicenow.table_api._table_collection_response import (
    TableCollectionResponse
)

_E = TypeVar("_E", bound=TableEntry)


class TablePageIterator(AbstractPageIterator[_E], Generic[_E]):
    """A class that iterates over pages of table items in the ServiceNow SDK.
    """

    def _fetch_page(self, uri: str) -> TableCollectionResponse[_E]:
        """
        Fetches a page of table items.

        Args:
            uri (str): The URI of the page to fetch.

        Returns:
            TableCollectionResponse[_E]: The response from the GET request.

        Raises:
            ValueError: If the URI is empty or None.
        """

        if not isinstance(uri, Optional[str]):
            raise TypeError("URI must be a string")

        if uri == "" or uri is None:
            raise ValueError(
                "URI cannot be empty or None. Please provide a valid URI."
            )

        req_info = RequestInformation()
        req_info.method = HTTPMethod.GET
        req_info.set_uri(uri)

        resp = self.client.send(req_info, None, TableCollectionResponse[_E])

        return resp
