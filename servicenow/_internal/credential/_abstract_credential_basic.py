from base64 import b64encode
from abc import ABC, abstractmethod
from typing import Tuple

from servicenow._internal.credential._abstract_credential import (
    AbstractCredential
)


class AbstractBasicCredential(AbstractCredential, ABC):

    def get_auth_type(self) -> str:

        return "basic"

    def get_authorization(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        username, password = self._request_credentials()

        auth = f"{username}:{password}"
        auth_bytes = bytes(auth, 'utf-8')

        return b64encode(auth_bytes).decode("ascii")

    @abstractmethod
    def _request_credentials(self) -> Tuple[str, str]:
        return NotImplemented
