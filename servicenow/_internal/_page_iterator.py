from abc import ABC, abstractmethod
from typing import Callable, Generic, TypeVar

from servicenow._internal._page_result import PageResult
from servicenow._internal._client import IClient
from servicenow._internal._abstract_collection_response import (
    ICollectionResponse
)

_E = TypeVar("_E")


class AbstractPageIterator(ABC, Generic[_E]):
    current_page: PageResult[_E]
    client: IClient
    pause_index: int

    def __init__(
        self,
        current_page: ICollectionResponse[_E],
        client: IClient,
    ) -> None:
        super().__init__()

        self.current_page = current_page.to_page()
        self.client = client
        self.pause_index = 0

    def next(self) -> None:
        """_summary_
        """

        next_page = self._fetch_and_convert_page(self.current_page.next_link)
        self.current_page = next_page
        self.pause_index = 0

    def prev(self) -> PageResult[_E]:

        prev_page = self._fetch_and_convert_page(self.current_page.prev_link)
        self.current_page = prev_page
        self.pause_index = 0

    def last(self) -> PageResult[_E]:

        last_page = self._fetch_and_convert_page(self.current_page.last_link)
        self.current_page = last_page
        self.pause_index = 0

    def first(self) -> PageResult[_E]:

        first_page = self._fetch_and_convert_page(self.current_page.first_link)
        self.current_page = first_page
        self.pause_index = 0

    def reverse(self, callback: Callable[[_E], bool]) -> None:

        if not callable(callback):
            raise Exception("callback must be callable")

        while True:
            keep_iterating = self._enumerate(callback)

            if not keep_iterating:
                return

            if self.current_page.prev_link == "":
                return

            self.prev()

    def iterate(self, callback: Callable[[_E], bool]) -> None:

        if not callable(callback):
            raise Exception("callback must be callable")

        while True:
            keep_iterating = self._enumerate(callback)

            if not keep_iterating:
                return

            if self.current_page.next_link == "":
                return

            self.next()

    def _fetch_and_convert_page(self, uri: str) -> PageResult[_E]:

        resp = self._fetch_page(uri)

        return resp.to_page()

    @abstractmethod
    def _fetch_page(self, uri: str) -> ICollectionResponse[_E]:
        return NotImplemented

    def _enumerate(self, callback: Callable[[_E], bool]) -> bool:

        keep_iterating = True

        page_items = self.current_page.items
        if page_items is None or len(page_items) == 0:
            return False

        for i in range(self.pause_index, len(page_items)):
            keep_iterating = callback(page_items[i])

            if not keep_iterating:
                break

            self.pause_index = i + 1
        return keep_iterating
