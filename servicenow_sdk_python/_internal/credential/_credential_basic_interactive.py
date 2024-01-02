from dataclasses import dataclass
from typing import Callable, Tuple
from servicenow_sdk_python._internal.credential._abstract_credential_basic import (
    AbstractBasicCredential
)


@dataclass
class InteractiveBasicCredential(AbstractBasicCredential):
    """
    This class inherits from the AbstractBasicCredential class and implements
    the _request_credentials method.
    It uses a callback function to request credentials.
    """

    callback: Callable[[], Tuple[str, str]]
    """
    A callback function that returns the username and password when called.
    """

    def _request_credentials(self) -> Tuple[str, str]:
        """
        This method calls the callback function to get the username and
        password.

        Returns:
            Tuple[str, str]: The username and password.
        """
        return self.callback()
