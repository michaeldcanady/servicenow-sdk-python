from dataclasses import dataclass
from typing import List

from servicenow._internal._query_parameter import QueryParameter

from servicenow.table_api._display_value import DisplayValue
from servicenow.table_api._view import View


@dataclass
class TableRequestBuilderPostQueryParameters(QueryParameter):
    sysparm_display_value: DisplayValue = None
    sysparm_exclude_reference_link: bool = None
    sysparm_fields: List[str] = None
    sysparm_input_display_value: bool = None
    sysparm_view: View = None
