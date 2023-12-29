from abc import ABC, abstractmethod


class AbstractCredential(ABC):

    def __init__(self) -> None:
        super().__init__()

    def get_authentication(self) -> str:

        return f"{self.get_auth_type()} {self.get_authorization()}"

    @abstractmethod
    def get_auth_type(self) -> str: ...

    @abstractmethod
    def get_authorization(self) -> str: ...
