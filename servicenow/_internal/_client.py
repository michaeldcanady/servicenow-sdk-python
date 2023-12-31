from abc import ABC, abstractmethod
from typing import Type
from httpx import Request

from servicenow._internal._request_information import RequestInformation


class IClient(ABC):

    @abstractmethod
    def to_request(self, req_info: RequestInformation) -> Request: ...

    @abstractmethod
    async def send(
        self,
        req_info: RequestInformation,
        error_mapping,
        response_type: Type,
    ): ...
