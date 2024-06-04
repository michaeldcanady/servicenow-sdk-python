"""Houses Service-Now Client
"""

from typing import Any, Type, TypeVar, Protocol, Union
from httpx import Client, Headers, Request, Response
from pydantic import BaseModel

from servicenow._internal import (
    IClient,
    RequestInformation,
)
from servicenow._internal.credential._abstract_credential import (
    AbstractCredential
)
from servicenow._internal.api_error import APIError

_A = TypeVar("_A", bound=BaseModel)
_A_co = TypeVar("_A_co", bound=BaseModel, covariant=True)


class _SupportsParseHeaders(Protocol):
    """Class that supports header parsing
    """

    def parse_headers(self, headers: Headers) -> None:
        """Parses the provided headers

        Args:
            headers (Headers): The response headers
        """


class _SupportsModelValidationJSON(Protocol[_A_co]):
    """Class that supports model validation JSON
    """

    @classmethod
    def model_validate_json(
        cls: type[_A],
        json_data: str | bytes | bytearray,
        *,
        strict: bool | None = None,
        context: dict[str, Any] | None = None,
    ) -> _A:
        """Usage docs:
        https://docs.pydantic.dev/2.5/concepts/json/#json-parsing

        Validate the given JSON data against the Pydantic model.

        Args:
            json_data: The JSON data to validate.
            strict: Whether to enforce types strictly.
            context: Extra variables to pass to the validator.

        Returns:
            The validated Pydantic model.

        Raises:
            ValueError: If `json_data` is not a JSON string.
        """


class _ReponseProtocol(_SupportsModelValidationJSON, _SupportsParseHeaders):
    pass


_R = TypeVar(
    "_R",
    bound=Union[_SupportsParseHeaders, _SupportsModelValidationJSON[Any]]
)


class ServiceNowClient(IClient):  # pylint:disable=too-few-public-methods
    """Service-Now HTTP Client.
    """

    base_url: str
    """The base URL for the Service-Now API.
    """

    credential: AbstractCredential
    """The credentials for the Service-Now API.
    """

    _client: Client
    """The HTTP client.
    """

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
        response_type: Type[_ReponseProtocol],
    ) -> _ReponseProtocol:
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

        request = self.to_request(req_info)

        raw_resp: Response = self._client.send(request)

        if raw_resp.is_error:
            raise APIError("error")
        resp: _ReponseProtocol = response_type.model_validate_json(raw_resp.text)
        resp.parse_headers(raw_resp.headers)

        return resp
