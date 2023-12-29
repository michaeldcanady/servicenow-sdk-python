from dataclasses import dataclass
from typing import List

from servicenow._internal._query_parameter import QueryParameter

from servicenow.table_api._display_value import DisplayValue
from servicenow.table_api._view import View


@dataclass
class TableRequestBuilderGetQueryParameters(QueryParameter):
    sysparm_display_value: DisplayValue = None
    sysparm_exclude_reference_link: bool = None
    sysparm_fields: List[str] = None
    sysparm_query_no_domain: bool = None
    sysparm_view: View = None
    sysparm_limit: int = None
    sysparm_no_count: bool = None
    sysparm_offset: int = None
    sysparm_query: str = None
    sysparm_query_category: str = None
    sysparm_suppress_pagination_header: bool = None
