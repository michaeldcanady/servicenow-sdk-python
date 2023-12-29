import re
from typing import List, Optional, TypeVar
from httpx import Headers

from servicenow._internal._response import AbstractResponse
from servicenow._internal._page_result import PageResult


_E = TypeVar("_E")


class TableCollectionResponse[_E](AbstractResponse[_E]):

    result: List[_E] = []
    next_link: Optional[str] = None
    prev_link: Optional[str] = None
    first_link: Optional[str] = None
    last_link: Optional[str] = None

    def parse_headers(self, headers: Headers) -> None:
        """_summary_

        Args:
            headers (Headers): _description_
        """

        regex = re.compile('<([^>]+)>;rel="([^"]+)"')

        links_header = headers["Link"]

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
        """_summary_

        Returns:
            PageResult[_E]: _description_
        """

        return PageResult(
            items=self.result,
            next_link=self.next_link,
            prev_link=self.prev_link,
            first_link=self.first_link,
            last_link=self.last_link,
        )
