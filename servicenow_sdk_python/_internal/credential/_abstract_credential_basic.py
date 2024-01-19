from base64 import b64encode
from abc import ABC, abstractmethod
from typing import Tuple

from servicenow_sdk_python._internal.credential._abstract_credential import (
    AbstractCredential
)


class AbstractBasicCredential(AbstractCredential, ABC):
    """
    This method returns the authorization string which is a base64 encoded
    string of the username and password.

    Returns:
        str: The base64 encoded authorization string.
    """

    def get_auth_type(self) -> str:
        """
        This method returns the type of authentication as 'basic'.

        Returns:
            str: The type of authentication.
        """

        return "basic"

    def get_authorization(self) -> str:
        """
        This method returns the authorization string which is a base64 encoded
        string of the username and password.

        Returns:
            str: The base64 encoded authorization string.
        """

        username, password = self._request_credentials()

        auth = f"{username}:{password}"
        auth_bytes = bytes(auth, 'utf-8')

        return b64encode(auth_bytes).decode("ascii")

    @abstractmethod
    def _request_credentials(self) -> Tuple[str, str]:
        """
        It should return the username and password.

        Returns:
            Tuple[str, str]: The username and password.
        """

        return NotImplemented
