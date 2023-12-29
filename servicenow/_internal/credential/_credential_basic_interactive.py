from typing import Callable, Tuple
from servicenow._internal.credential._abstract_credential_basic import (
    AbstractBasicCredential
)


class InteractiveBasicCredential(AbstractBasicCredential):

    _callback: Callable[[], Tuple[str, str]]

    def __init__(self, callback: Callable[[], Tuple[str, str]]) -> None:
        super().__init__()

        self._callback = callback

    def _request_credentials(self) -> Tuple[str, str]:
        """_summary_

        Returns:
            Tuple[str, str]: _description_
        """

        return self._callback()
