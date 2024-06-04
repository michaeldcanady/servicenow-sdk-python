from enum import IntEnum, auto


class HTTPMethod(IntEnum):
    """Enum of support HTTP methods
    """

    NONE = 0
    """no HTTP method selected"""

    GET = auto()
    """represents GET method"""

    POST = auto()
    """represents POST method"""

    PUT = auto()
    """represents PUT method"""

    HEAD = auto()
    """represents HEAD method"""

    OPTIONS = auto()
    """represents OPTIONS method"""

    DELETE = auto()
    """represents DELETE method"""

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
