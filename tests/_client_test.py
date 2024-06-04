import pytest
from httpx import Headers, Request

from servicenow._internal._request_information import (
    RequestInformation
)
from servicenow._internal._uri_information import URIInformation
from servicenow._internal._http_method import HTTPMethod
from servicenow._internal._collection import Collection

from servicenow.credential import (
    UsernamePasswordCredential,
    SecureString,
)
from servicenow._client import ServiceNowClient


@pytest.fixture
def sn_client(pytestconfig):
    credential = UsernamePasswordCredential()
    credential.username = SecureString(pytestconfig.getoption("username"))
    credential.password = SecureString(pytestconfig.getoption("password"))
    return ServiceNowClient(
        credential=credential,
        instance="test.service-now.com/api",
    )


def test_to_request(sn_client: ServiceNowClient):
    req_info = RequestInformation()
    req_info.method = HTTPMethod.GET
    req_info.content = b"test content"
    req_info._headers = Headers({"Content-Type": "application/json"})
    uri_info = URIInformation()
    uri_info.template = "{+baseurl}/path"
    uri_info.path = Collection(baseurl="http://example.com")
    req_info._uri = uri_info

    req = sn_client.to_request(req_info)
    assert isinstance(req, Request)
    assert req.method == "GET"
    assert req.url == "http://example.com/path"
    assert req.headers == Headers({
        "host": "example.com",
        "Content-Length": str(len(req_info.content)),
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Basic dXNlcjpwYXNz"
    })
    assert req.content == b"test content"
