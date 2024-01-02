import pytest
from httpx import Headers, Request

from servicenow_sdk_python._internal._http_method import HTTPMethod
from servicenow_sdk_python._internal._uri_information import URIInformation
from servicenow_sdk_python._internal._request_information import RequestInformation
from servicenow_sdk_python._internal._collection import Collection


@pytest.fixture
def req_info():
    return RequestInformation()


def test_method_property(req_info: RequestInformation):
    req_info.method = HTTPMethod.GET
    assert req_info.method == HTTPMethod.GET


def test_headers_property(req_info: RequestInformation):
    headers = Headers({"Content-Type": "application/json"})
    req_info._headers = headers
    assert req_info.headers == headers


def test_content_property(req_info: RequestInformation):
    content = b"test content"
    req_info.content = content
    assert req_info.content == content


def test_uri_property(req_info: RequestInformation):
    uri_info = URIInformation()
    req_info._uri = uri_info
    assert req_info.uri == uri_info


def test_to_request(req_info: RequestInformation):
    req_info.method = HTTPMethod.GET
    req_info.content = b"test content"
    req_info._headers = Headers({"Content-Type": "application/json"})
    uri_info = URIInformation()
    uri_info.template = "{+baseurl}/path"
    uri_info.path = Collection(baseurl="http://example.com")
    req_info._uri = uri_info

    req = req_info.to_request()
    assert isinstance(req, Request)
    assert req.method == "GET"
    assert req.url == "http://example.com/path"
    assert req.headers == Headers(
        {
            "host": "example.com",
            "Content-Type": "application/json",
            "Content-Length": str(len(req_info.content)),
        }
    )
    assert req.content == b"test content"
