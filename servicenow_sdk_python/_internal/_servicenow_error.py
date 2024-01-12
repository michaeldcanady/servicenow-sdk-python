from pydantic import BaseModel


class Error(BaseModel):

    detail: str
    message: str

    def __str__(self) -> str:
        return f"detail: {self.detail}, message: {self.message}"


class ServiceNowError(BaseModel):

    error: Error
    status: str

    def exception(self) -> Exception:

        return Exception(str(self))

    def __str__(self) -> str:

        return f"error: {self.error}, status: {self.status}"


class AuthError(ServiceNowError):
    pass
