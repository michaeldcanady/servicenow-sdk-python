from dataclasses import dataclass
from typing import List
from servicenow_sdk_python._internal._query_parameter import QueryParameter
from servicenow_sdk_python.table_api._display_value import DisplayValue
from servicenow_sdk_python.table_api._view import View


@dataclass
class TableItemPutQueryParameters(QueryParameter):

    sysparm_display_value: DisplayValue = DisplayValue.NONE
    sysparm_exclude_reference_link: bool = None
    sysparm_fields: List[str] = None
    sysparm_input_display_value: bool = None
    sysparm_query_no_domain: bool = None
    sysparm_view: View = View.NONE
