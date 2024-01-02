from typing import Tuple
from servicenow_sdk_python._internal.credential._credential_basic_interactive import (
    InteractiveBasicCredential,
)

# TODO: Find a way to properly secure password?


class SecureString(str):

    def __repr__(self) -> str:
        return "[secure]"


class UsernamePasswordCredential(InteractiveBasicCredential):
    username: SecureString
    password: SecureString

    def __init__(self) -> None:
        super().__init__(self._prompt_for_creds)

        self.username = None
        self.password = None

    def get_auth_type(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        return "Basic"

    def _prompt_for_creds(self) -> Tuple[str, str]:
        """_summary_

        Returns:
            Tuple[str,str]: _description_
        """

        while (self.username == "" or self.username is None) and (
            self.password == "" or self.password is None
        ):
            self.username = SecureString(input("username: "))
            self.password = SecureString(input("password: "))
        return self.username, self.password
