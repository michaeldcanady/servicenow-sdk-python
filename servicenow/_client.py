from typing import Any, TypeVar, Protocol, Union
from servicenow._internal.credential._abstract_credential import (
    AbstractCredential
)
from httpx import Client, Headers, Request, Response

from servicenow._internal._client import IClient
from servicenow._internal._request_information import RequestInformation

_A = TypeVar("_A")


class SupportsParseHeaders(Protocol):

    def parse_headers(self, headers: Headers) -> None: ...


class SupportsModelValidationJSON(Protocol[_A]):

    def model_validate_json() -> _A: ...


_R = TypeVar(
    "_R",
    bound=Union[SupportsParseHeaders, SupportsModelValidationJSON[Any]]
)


class ServiceNowClient(IClient):

    base_url: str
    credential: AbstractCredential
    _client: Client

    def __init__(
        self,
        credential: AbstractCredential,
        instance: str,
    ) -> None:

        self.credential = credential

        if instance is None or instance == "":
            raise ValueError("instance cannot be empty")

        if not instance.endswith(".service-now.com/api"):
            instance += ".service-now.com/api"

        if not instance.startswith("https://"):
            instance = "https://" + instance

        self.base_url = instance
        self._client = Client()

        super().__init__()

    def to_request(self, req_info: RequestInformation) -> Request:
        """Converts req info to a Request

        Args:
            req_info (RequestInformation): The Request Information

        Returns:
            Request: The generated Request.
        """

        if not isinstance(req_info, RequestInformation):
            raise TypeError("req_info must be of type RequestInformation")

        request = req_info.to_request()

        auth_header = self.credential.get_authentication()

        request.headers.update({"Authorization": auth_header})
        request.headers.update({"Content-Type": "application/json"})
        request.headers.update({"Accept": "application/json"})
        return request

    def send(
        self,
        req_info: RequestInformation,
        error_mapping,
        response_type: _R,
    ) -> _R:

        request = self.to_request(req_info)

        raw_resp: Response = self._client.send(request)

        if raw_resp.is_error:
            raise Exception("error")
        resp: _R = response_type.model_validate_json(raw_resp.text)
        resp.parse_headers(raw_resp.headers)

        return resp
