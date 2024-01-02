from abc import ABC, abstractmethod


class AbstractCredential(ABC):
    """
    This is an abstract base class for handling credentials.
    """

    def get_authentication(self) -> str:
        """
        This method returns the authentication string which is a combination
        of the auth type and authorization.

        Returns:
            str: The authentication string.
        """

        return f"{self.get_auth_type()} {self.get_authorization()}"

    @abstractmethod
    def get_auth_type(self) -> str:
        """
        It should return the type of authentication.

        Returns:
            str: The type of authentication.
        """

    @abstractmethod
    def get_authorization(self) -> str:
        """
        It should return the type of authentication.

        Returns:
            str: The type of authentication.
        """
