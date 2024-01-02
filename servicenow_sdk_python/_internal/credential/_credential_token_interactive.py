from typing import Callable
from servicenow_sdk_python._internal.credential._abstract_credential_token import (
    AbstractTokenCredential
)


class InteractiveTokenCredential(AbstractTokenCredential):

    _callback: Callable[[], str]

    def __init__(self, callback: Callable[[], str]) -> None:
        super().__init__()

        self._callback = callback

    def _request_credentials(self) -> str:
        """_summary_

        Returns:
            Tuple[str, str]: _description_
        """

        return self._callback()
