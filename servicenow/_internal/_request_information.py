from typing import Optional, Union
from httpx import Headers, Request

from servicenow._internal._http_method import HTTPMethod
from servicenow._internal._uri_information import URIInformation, _RAW_URL_KEY
from servicenow._internal._collection import Collection


class RequestInformation:
    _method: HTTPMethod
    _headers: Headers
    _content: Optional[bytes]
    _uri: URIInformation

    def __init__(self) -> None:
        self._method = HTTPMethod.NONE
        self._headers = Headers()
        self._content = None
        self._uri = URIInformation()

    @property
    def method(self) -> HTTPMethod:
        return self._method

    @method.setter
    def method(self, method: Union[int, HTTPMethod]) -> None:

        if not isinstance(method, Union[int, HTTPMethod]):
            raise TypeError("method must be of type: int, or HTTPMethod")

        if isinstance(method, int):
            method = HTTPMethod(method)

        self._method = method

    @property
    def headers(self) -> Headers:
        return self._headers

    @property
    def content(self) -> Optional[bytes]:
        return self._content

    # TODO: make it marshal other types to JSON
    @content.setter
    def content(self, content: Optional[bytes]) -> None:
        if content is not None and not isinstance(content, bytes):
            raise TypeError("content must be of type: bytes or None")

        self._content = content

    @property
    def uri(self) -> URIInformation:
        return self._uri

    def to_request(self) -> Request:
        """_summary_

        Returns:
            Request: _description_
        """

        return Request(
            method=str(self._method),
            url=self._uri.to_url(),
            headers=self._headers,
            content=self._content,
        )

    def set_uri(self, uri: str) -> None:
        """_summary_

        Args:
            uri (str): _description_
        """

        collection = Collection()
        collection[_RAW_URL_KEY] = uri

        self.uri.path = collection
