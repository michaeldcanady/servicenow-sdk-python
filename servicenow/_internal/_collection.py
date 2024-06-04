from typing import Dict, TypeVar

_VT = TypeVar("_VT")


class Collection(Dict[str, _VT]):
    """Base collection type
    """

    def __init__(self, **kwargs) -> None:

        super().__init__()

        for key, value in kwargs.items():
            self[key] = value

    def __setitem__(self, __key: str, __value: _VT) -> None:

        __key = __key.lower()

        return super().__setitem__(__key, __value)

    def __getitem__(self, __key: str) -> _VT:

        __key = __key.lower()

        return super().__getitem__(__key)

    def __delitem__(self, __key: str) -> None:
        return super().__delitem__(__key)
