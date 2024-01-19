from abc import abstractmethod, ABC
from typing import Generic, TypeVar
from httpx import Headers
from pydantic import BaseModel


_E = TypeVar("_E")


class AbstractResponse(BaseModel, ABC, Generic[_E]):

    @abstractmethod
    def parse_headers(self, headers: Headers) -> None:
        """_summary_

        Args:
            headers (Headers): _description_
        """
