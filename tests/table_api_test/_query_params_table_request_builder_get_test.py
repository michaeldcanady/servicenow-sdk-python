from servicenow_sdk_python.table_api._display_value import DisplayValue
from servicenow_sdk_python.table_api._view import View
from servicenow_sdk_python.table_api._query_params_table_request_builder_get import (
    TableRequestBuilderGetQueryParameters,
)


def test_table_request_builder_get_query_parameters():
    # Create an instance of the dataclass
    query_parameters = TableRequestBuilderGetQueryParameters(
        sysparm_display_value=DisplayValue.ALL,
        sysparm_exclude_reference_link=True,
        sysparm_fields=["field1", "field2"],
        sysparm_query_no_domain=True,
        sysparm_view=View.BOTH,
        sysparm_limit=100,
        sysparm_no_count=True,
        sysparm_offset=0,
        sysparm_query="field=value",
        sysparm_query_category="category",
        sysparm_suppress_pagination_header=True,
    )

    # Check that the fields are correctly set
    assert query_parameters.sysparm_display_value == DisplayValue.ALL
    assert query_parameters.sysparm_exclude_reference_link is True
    assert query_parameters.sysparm_fields == ["field1", "field2"]
    assert query_parameters.sysparm_query_no_domain is True
    assert query_parameters.sysparm_view == View.BOTH
    assert query_parameters.sysparm_limit == 100
    assert query_parameters.sysparm_no_count is True
    assert query_parameters.sysparm_offset == 0
    assert query_parameters.sysparm_query == "field=value"
    assert query_parameters.sysparm_query_category == "category"
    assert query_parameters.sysparm_suppress_pagination_header is True
    assert query_parameters.to_query() == {
        "sysparm_display_value": "all",
        "sysparm_exclude_reference_link": "true",
        "sysparm_fields": "field1,field2",
        "sysparm_query_no_domain": "true",
        "sysparm_view": "both",
        "sysparm_limit": "100",
        "sysparm_no_count": "true",
        "sysparm_offset": "0",
        "sysparm_query": "field=value",
        "sysparm_query_category": "category",
        "sysparm_suppress_pagination_header": "true",
    }
