from typing import (
    Dict,
    Optional,
    TypeVar,
)

from servicenow._internal._http_method import HTTPMethod
from servicenow._internal._request_information import RequestInformation
from servicenow._internal._client import IClient
from servicenow._internal._request_configuration import RequestConfiguration
from servicenow._internal._response import AbstractResponse

_E = TypeVar("_E")
_RCT = TypeVar("_RCT", bound=RequestConfiguration)


class RequestBuilder[_E]():

    path_parameters: Dict[str, str]
    url_template: str
    client: IClient

    def __init__(
        self,
        path_parameters: Dict[str, str],
        client: IClient,
        url_template: str,
    ) -> None:
        super().__init__()

        self.path_parameters = path_parameters
        self.client = client
        self.url_template = url_template

    def send(
        self,
        method: HTTPMethod,
        config: _RCT,
    ) -> AbstractResponse[_E]:

        req_info = self.to_request_information(method, config)
        return self.client.send(
            req_info,
            config.mapping,
            type(config.response),
        )

    def send_get(
        self,
        config: _RCT,
    ) -> AbstractResponse[_E]:

        return self.send(HTTPMethod.GET, config)

    def send_put(
        self,
        config: _RCT,
    ) -> AbstractResponse[_E]:

        return self.send(HTTPMethod.PUT, config)

    def send_delete(
        self,
        config: _RCT,
    ) -> AbstractResponse[_E]:
        return self.send(HTTPMethod.DELETE, config)

    def send_post(
        self,
        config: _RCT,
    ) -> AbstractResponse[_E]:
        return self.send(HTTPMethod.POST, config)

    def to_request_information(
        self,
        method: HTTPMethod,
        config: Optional[_RCT] = None,
    ) -> RequestInformation:

        req_info = RequestInformation()

        if config:
            if config.query:
                req_info.uri.query = config.query.to_query()
            if config.headers:
                req_info.headers.update(config.headers)
            if config.data:
                req_info.content = bytes(
                    config.data.model_dump_json(),
                    'utf-8',
                )

        req_info.method = method
        req_info.uri.path = self.path_parameters
        req_info.uri.template = self.url_template

        return req_info
