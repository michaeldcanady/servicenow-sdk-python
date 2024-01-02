from dataclasses import dataclass
from typing import Any, Dict, Optional, Protocol, TypeAlias

from httpx import Headers

from servicenow_sdk_python._internal._query_parameter import QueryParameter

IncEx: TypeAlias = (
    'set[int] | set[str] | dict[int, Any] | dict[str, Any] | None'
)


class SupportsModelDumpJSON(Protocol):
    def model_dump_json(
        self,
        *,
        indent: int | None = None,
        include: IncEx = None,
        exclude: IncEx = None,
        by_alias: bool = False,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        round_trip: bool = False,
        warnings: bool = True
    ) -> str:
        ...


@dataclass
class RequestConfiguration:
    headers: Optional[Headers] = None
    query: QueryParameter = None
    data: SupportsModelDumpJSON = None
    mapping: Optional[Dict[str, str]] = None
    response: Any = None
