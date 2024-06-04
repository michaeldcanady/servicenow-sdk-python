from dataclasses import dataclass
from typing import List
from servicenow._internal._query_parameter import QueryParameter
from servicenow.table_api._display_value import DisplayValue
from servicenow.table_api._view import View


@dataclass
class TableItemGetQueryParameters(QueryParameter):
    """A class used to represent the query parameters for a GET table item
    request.
    """

    sysparm_display_value: DisplayValue = DisplayValue.NONE
    """Determines the type of data returned, either the actual values from the
    database or the display values of the fields. Display values are
    manipulated based on the actual value in the database and user or system
    settings and preferences.

    If returning display values, the value that is returned is dependent on
    the field type.
    Default is `DisplayValue.NONE`.
    """

    sysparm_exclude_reference_link: bool = None
    """Whether to exclude the reference link of the system parameter.
    Default is None.
    """

    sysparm_fields: List[str] = None
    """Comma-separated list of fields to return in the response.
    Default is None.
    """

    sysparm_query_no_domain: bool = None
    """Flag that indicates whether to restrict the record search to only the
    domains for which the logged in user is configured. Default is None.
    """

    sysparm_view: View = View.NONE
    """UI view for which to render the data.
    Determines the fields returned in the response. Default is View.NONE.
    """
