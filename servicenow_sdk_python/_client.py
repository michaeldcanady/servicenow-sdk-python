"""Houses Service-Now Client
"""

from typing import Any, TypeVar, Protocol, Union
from httpx import Client, Headers, Request, Response
from pydantic import BaseModel

from servicenow_sdk_python._internal import (
    IClient,
    RequestInformation,
)
from servicenow_sdk_python._internal.credential._abstract_credential import (
    AbstractCredential
)
from servicenow_sdk_python._internal._servicenow_error import (
    ServiceNowError,
    AuthError,
)
from servicenow_sdk_python._internal._error_map import ErrorMap

_A = TypeVar("_A", bound=BaseModel)


class _SupportsParseHeaders(Protocol):
    """Class that supports header parsing
    """

    def parse_headers(self, headers: Headers) -> None:
        """Parses the provided headers

        Args:
            headers (Headers): The response headers
        """


class _SupportsModelValidationJSON(Protocol[_A]):
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


_R = TypeVar(
    "_R",
    bound=Union[_SupportsParseHeaders, _SupportsModelValidationJSON[Any]]
)


class ServiceNowClient(IClient):
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
        """
        Converts request information to a Request.

        Args:
            req_info (RequestInformation): The request information.

        Returns:
            Request: The generated Request.

        Raises:
            TypeError: If `req_info` is not of type RequestInformation.
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
        """
        Sends a request and returns the response.

        Args:
            req_info (RequestInformation): The request information.
            error_mapping: The error mapping.
            response_type (_R): The type of the response.

        Returns:
            _R: The response.

        Raises:
            Exception: If the response is an error.
        """

        request = self.to_request(req_info)

        raw_resp: Response = self._client.send(request)

        raw_resp = self._to_error(raw_resp)
        resp: _R = response_type.model_validate_json(raw_resp.text)
        resp.parse_headers(raw_resp.headers)

        return resp

    def _to_error(self, resp: Response) -> Response:

        if not resp.is_error:
            return resp

        error_map = ErrorMap()
        error_map.set("401", AuthError)

        _err_type = error_map.get(resp.status_code)

        raise _err_type.model_validate_json(resp.text).exception()
