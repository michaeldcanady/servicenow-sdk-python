from typing import Tuple
from servicenow_sdk_python._internal.credential._abstract_credential_basic import (
    AbstractBasicCredential
)


class NonInteractiveBasicCredential(AbstractBasicCredential):

    username: str
    password: str

    def __init__(self, username: str, password: str) -> None:
        super().__init__()

        if not isinstance(username, str) or username == "":
            raise TypeError("username must be non-empty str")

        if not isinstance(password, str) or password == "":
            raise TypeError("password must be non-empty str")

        self.username = username
        self.password = password

    def _request_credentials(self) -> Tuple[str, str]:
        """_summary_

        Returns:
            Tuple[str, str]: _description_
        """

        return self.username, self.password
