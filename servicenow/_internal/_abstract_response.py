from abc import abstractmethod, ABC
from typing import Generic, TypeVar
from httpx import Headers
from pydantic import BaseModel


_E = TypeVar("_E")


class AbstractResponse(BaseModel, ABC, Generic[_E]):  # pylint:disable=too-few-public-methods
    """The base for all responses
    """

    @abstractmethod
    def parse_headers(self, headers: Headers) -> None:
        """Parses response headers

        Args:
            headers (Headers): The reponse headers
        """
