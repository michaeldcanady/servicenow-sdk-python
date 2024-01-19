import re
from typing import Type
from servicenow_sdk_python._internal._servicenow_error import _ServiceNowError


class ErrorMap:

    slots = ["__dict__"]

    def __init__(self) -> None:

        self.__dict__ = {}

    def set(self, key: str, value: _ServiceNowError) -> None:
        """_summary_

        Args:
            key (str): _description_
            value (ServiceNowError): _description_
        """

        transformed_key = key.replace('X', '[0-9]')

        self.__dict__[transformed_key] = value

    def get(self, status_code: int) -> Type[_ServiceNowError]:
        """_summary_

        Args:
            status_code (int): _description_

        Returns:
            ServiceNowError: _description_
        """

        code_str = str(status_code)

        for key, value in self.__dict__.items():
            if re.match(key, code_str):
                return value
        return _ServiceNowError
