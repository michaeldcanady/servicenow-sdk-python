""" Houses Items for Current User requests
"""
from typing import Dict, Optional
from dataclasses import dataclass

from httpx import Headers
from pydantic import BaseModel, Field
from servicenow._internal import (
    AbstractItemResponse,
    IClient,
    RequestBuilder,
    RequestConfiguration,
)


class CurrentUser(BaseModel):
    """A class used to represent teh current user."""

    avatar: str = Field(alias="user_avatar")
    """The avatar of the user."""

    sys_id: str = Field(alias="user_sys_id")
    """The system ID of the user."""

    name: str = Field(alias="user_name")
    """The name of the user."""

    display_name: str = Field(alias="user_display_name")
    """The display name of the user."""

    intials: str = Field(alias="user_initials")
    """The initials of the user."""


class CurrentUserItemResponse(AbstractItemResponse[CurrentUser]):
    """A class used to represent the respone of the current user item."""

    result: Optional[CurrentUser] = None
    """The result of the current user item."""

    def parse_headers(self, headers: Headers) -> None:
        """_summary_

        Args:
            headers (Headers): _description_
        """


@dataclass
class CurrentUserGetRequestConfigurations(RequestConfiguration):
    """A class used to represent the configurations of the current user get
    request.
    """

    headers: Optional[Headers] = None
    """The headers of the request."""

    query = None
    """The query of the request."""

    data = None
    """The data of the request."""

    mapping: Optional[Dict[str, str]] = None
    """The error mapping of the request."""

    response: Optional[CurrentUserItemResponse] = None
    """The response of the request."""


class CurrentUserRequestBuilder(RequestBuilder[CurrentUser]):
    """A class used to build the request of the current user."""

    def __init__(
        self,
        path_parameters: Dict[str, str],
        client: IClient,
    ) -> None:
        base_url = path_parameters["baseurl"]

        if not base_url.endswith("/now"):
            path_parameters["baseurl"] = base_url + "/now"

        super().__init__(
            path_parameters,
            client,
            "{+baseurl}/ui/user/current_user",
        )

    def get(self) -> CurrentUserItemResponse:
        """
        Sends a GET request.

        Returns:
            CurrentUserItemResponse: The response of the GET request.
        """

        config = CurrentUserGetRequestConfigurations(
            response=CurrentUserItemResponse()
        )

        return self.send_get(config)
