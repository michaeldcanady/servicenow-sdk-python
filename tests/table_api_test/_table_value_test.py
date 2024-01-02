from servicenow_sdk_python.table_api._table_value import TableValue


def test_table_value_all():
    test_data = {
        "link": "link",
        "value": "value",
        "display_value": "display value",
    }

    value = TableValue(**test_data)

    assert value.link == "link"
    assert value.value == "value"
    assert value.display_value == "display value"


def test_table_value_display_value():
    test_data = {
        "link": "link",
        "display_value": "display value",
    }

    value = TableValue(**test_data)

    assert value.link == "link"
    assert value.value is None
    assert value.display_value == "display value"


def test_table_value_display_value_exclude_ref_link():
    test_data = "display value"

    value = TableValue(**test_data)

    assert value.link is None
    assert value.value is None
    assert value.display_value == "display value"
