import re
from typing import Generic, List, Optional, TypeVar
from httpx import Headers

from servicenow_sdk_python._internal._abstract_collection_response import (
    ICollectionResponse
)
from servicenow_sdk_python._internal._page_result import PageResult


_E = TypeVar("_E")


class TableCollectionResponse(ICollectionResponse[_E], Generic[_E]):
    """A class used to represent the response of a table collection.
    """

    result: List[_E] = []
    """The result of the table collection."""

    next_link: Optional[str] = None
    """The next link of the table collection."""

    prev_link: Optional[str] = None
    """The previous link of the table collection."""

    first_link: Optional[str] = None
    """The first link of the table collection."""

    last_link: Optional[str] = None
    """The last link of the table collection."""

    def parse_headers(self, headers: Headers) -> None:
        """Parses the headers.

        Args:
            headers (Headers): The headers to parse.
        """

        regex = re.compile('<([^>]+)>;rel="([^"]+)"')

        links_header = headers.get("Link", None)
        if links_header is None:
            return

        link_matches = regex.findall(links_header, -1)

        for match in link_matches:
            link = match[0]
            rel = match[1]

            match rel:
                case "first":
                    self.first_link = link
                case "prev":
                    self.prev_link = link
                case "next":
                    self.next_link = link
                case "last":
                    self.last_link = link

    def to_page(self) -> PageResult[_E]:
        """
        Converts the table collection response to a page result.

        Returns:
            PageResult[_E]: The page result.
        """

        return PageResult(
            items=self.result,
            next_link=self.next_link,
            prev_link=self.prev_link,
            first_link=self.first_link,
            last_link=self.last_link,
        )
