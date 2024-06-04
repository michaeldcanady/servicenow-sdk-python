from servicenow.table_api._display_value import DisplayValue


def test_display_value_none_str():

    display_value = DisplayValue.NONE

    assert str(display_value) == ""


def test_display_value_true_str():

    display_value = DisplayValue.TRUE

    assert str(display_value) == "true"


def test_display_value_false_str():

    display_value = DisplayValue.FALSE

    assert str(display_value) == "false"


def test_display_value_all_str():

    display_value = DisplayValue.ALL

    assert str(display_value) == "all"
