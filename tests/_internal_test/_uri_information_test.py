import pytest

from servicenow_sdk_python._internal._collection import Collection
from servicenow_sdk_python._internal._uri_information import URIInformation


@pytest.fixture
def uri_info():
    return URIInformation()


def test_path_property(uri_info: URIInformation):
    path_collection = Collection(baseurl="http://example.com")
    uri_info.path = path_collection
    assert uri_info.path == path_collection


def test_query_property(uri_info: URIInformation):
    query_collection = Collection(param="value")
    uri_info.query = query_collection
    assert uri_info.query == query_collection


def test_template_property(uri_info: URIInformation):
    template_str = "{+baseurl}/path"
    uri_info.template = template_str
    assert uri_info.template == template_str


def test_get_uri_from_raw_with_raw(uri_info: URIInformation):
    uri_info.path = Collection(
        baseurl="http://example.com",
        **{"request-raw-url": "http://example.com/raw"},
    )
    assert uri_info._get_uri_from_raw() == "http://example.com/raw"


def test_get_uri_from_raw_without_raw(uri_info: URIInformation):
    uri_info.path = Collection(
        baseurl="http://example.com",
    )
    assert uri_info._get_uri_from_raw() == ""


def test_build_uri_template(uri_info: URIInformation):
    uri_info.path = Collection(baseurl="http://example.com")
    uri_info.query = Collection(param="value")
    uri_info.template = "{+baseurl}/path{?param}"
    assert uri_info._build_uri() == "http://example.com/path?param=value"


def test_build_uri_raw(uri_info: URIInformation):
    uri_info.path = Collection(baseurl="http://example.com")
    uri_info.query = Collection(param="value")
    uri_info.template = "{+baseurl}/path{?param}"
    assert uri_info._build_uri() == "http://example.com/path?param=value"


def test_to_url(uri_info: URIInformation):
    uri_info.path = Collection(
        baseurl="http://example.com",
        **{"request-raw-url": "http://example.com/raw"},
    )
    assert uri_info.to_url() == "http://example.com/raw"

    uri_info.path = Collection(baseurl="http://example.com")
    uri_info.query = Collection(param="value")
    uri_info.template = "{+baseurl}/path{?param}"
    assert uri_info.to_url() == "http://example.com/path?param=value"
