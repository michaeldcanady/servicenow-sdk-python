from dataclasses import dataclass
from typing import Generic, List, Optional, TypeVar

_E = TypeVar("_E")


@dataclass
class PageResult(Generic[_E]):
    items: List[_E]
    next_link: Optional[str]
    prev_link: Optional[str]
    first_link: Optional[str]
    last_link: Optional[str]
