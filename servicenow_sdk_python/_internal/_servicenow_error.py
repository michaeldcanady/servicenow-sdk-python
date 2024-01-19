from __future__ import annotations
from pydantic import BaseModel


class ServiceNowError(Exception):

    def __init__(self, service_error: _ServiceNowError) -> None:
        super().__init__(None)
        self._service_error = service_error

    def __str__(self) -> str:
        return str(self._service_error)

class AuthError(ServiceNowError):
    pass


class _Error(BaseModel):

    detail: str
    message: str

    def __str__(self) -> str:
        return f"detail: {self.detail}, message: {self.message}"


class _ServiceNowError(BaseModel):

    error: _Error
    status: str

    def exception(self) -> ServiceNowError:

        return ServiceNowError(str(self))

    def __str__(self) -> str:

        return f"error: {self.error}, status: {self.status}"


class _AuthError(_ServiceNowError):

    def exception(self) -> AuthError:
        return AuthError(str(self))
