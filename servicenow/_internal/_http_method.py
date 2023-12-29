from enum import IntEnum, auto


class HTTPMethod(IntEnum):

    NONE = 0
    GET = auto()
    POST = auto()
    PUT = auto()
    HEAD = auto()
    OPTIONS = auto()
    DELETE = auto()

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        return [
            "",
            "GET",
            "POST",
            "PUT",
            "HEAD",
            "OPTIONS",
            "DELETE",
        ][self]
