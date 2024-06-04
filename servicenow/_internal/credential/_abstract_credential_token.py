from abc import ABC, abstractmethod

from servicenow._internal.credential._abstract_credential import (
    AbstractCredential
)


class AbstractTokenCredential(AbstractCredential, ABC):

    def get_auth_type(self) -> str:

        return "token"

    def get_authorization(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        token = self._request_token()

        return f"bearer {token}"

    @abstractmethod
    def _request_token(self) -> str:
        return NotImplemented
