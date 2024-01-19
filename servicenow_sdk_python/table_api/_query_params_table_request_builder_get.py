from dataclasses import dataclass
from typing import List

from servicenow_sdk_python._internal._query_parameter import QueryParameter

from servicenow_sdk_python.table_api._display_value import DisplayValue
from servicenow_sdk_python.table_api._view import View


@dataclass
class TableRequestBuilderGetQueryParameters(QueryParameter):
    """A class used to represent the query parameters for a GET table
    collection request.
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

    sysparm_view: View = None
    """UI view for which to render the data.
    Determines the fields returned in the response. Default is View.NONE.
    """

    sysparm_limit: int = None
    """Maximum number of records to return. For requests that exceed this
    number of records, use the sysparm_offset parameter to paginate record
    retrieval.

    This limit is applied before ACL evaluation. If no records return,
    including records you have access to, rearrange the record order so
    records you have access to return first. Default is None
    """
    sysparm_no_count: bool = None
    """Flag that indicates whether to execute a select count(*) query on the
    table to return the number of rows in the associated table.
    Default is None.
    """

    sysparm_offset: int = None
    """Starting record index for which to begin retrieving records. Use this
    value to paginate record retrieval. This functionality enables the
    retrieval of all records, regardless of the number of records, in small
    manageable chunks. Default is None.
    """

    sysparm_query: str = None
    """Encoded query used to filter the result set.
    You can use a UI filter to obtain a properly encoded query.
    Default is None.
    """

    sysparm_query_category: str = None
    """Name of the category to use for queries.
    """

    sysparm_query_no_domain: bool = None
    """Flag that indicates whether to restrict the record search to only the
    domains for which the logged in user is configured. Default is None.
    """

    sysparm_suppress_pagination_header: bool = None
    """Flag that indicates whether to remove the Link header from the response.
    The Link header provides various URLs to relative pages in the record set
    which you can use to paginate the returned record set.
    Default is None.
    """

    sysparm_view: View = View.NONE
    """UI view for which to render the data.
    Determines the fields returned in the response. Default is View.NONE.
    """
