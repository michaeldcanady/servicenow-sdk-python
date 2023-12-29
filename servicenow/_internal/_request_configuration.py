from dataclasses import dataclass
from typing import Any, Dict, Optional

from httpx import Headers

from servicenow._internal._query_parameter import QueryParameter


@dataclass
class RequestConfiguration:
    headers: Optional[Headers] = None
    query: QueryParameter = None
    data: Any = None
    mapping: Optional[Dict[str, str]] = None
    response: Any = None
