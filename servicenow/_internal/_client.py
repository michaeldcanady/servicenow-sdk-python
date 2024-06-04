from abc import ABC, abstractmethod
from ast import TypeVar
from typing import Type
from httpx import Request

from servicenow._internal._request_information import (
    RequestInformation
)

_R = TypeVar("_R")


class IClient(ABC):

    @abstractmethod
    def to_request(self, req_info: RequestInformation) -> Request:
        """
        Converts request information to a Request.

        Args:
            req_info (RequestInformation): The request information.

        Returns:
            Request: The generated Request.

        Raises:
            TypeError: If `req_info` is not of type RequestInformation.
        """

    @abstractmethod
    def send(
        self,
        req_info: RequestInformation,
        error_mapping,
        response_type: Type[_R],
    ) -> _R:
        """
        Sends a request and returns the response.

        Args:
            req_info (RequestInformation): The request information.
            error_mapping: The error mapping.
            response_type Type[_ReponseProtocol]: The type of the response.

        Returns:
            _ReponseProtocol: The response.

        Raises:
            APIError: If the response is an error.
        """
