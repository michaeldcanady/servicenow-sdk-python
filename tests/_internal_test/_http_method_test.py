from servicenow._internal._http_method import HTTPMethod


def test_http_method_none():

    assert str(HTTPMethod.NONE) == ""


def test_http_method_get():

    assert str(HTTPMethod.GET) == "GET"


def test_http_method_post():

    assert str(HTTPMethod.POST) == "POST"


def test_http_method_put():
    assert str(HTTPMethod.PUT) == "PUT"


def test_http_method_head():
    assert str(HTTPMethod.HEAD) == "HEAD"


def test_http_method_options():
    assert str(HTTPMethod.OPTIONS) == "OPTIONS"


def test_http_method_delete():
    assert str(HTTPMethod.DELETE) == "DELETE"
