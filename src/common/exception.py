# src/common/exception.py

from fastapi import HTTPException


class BaseException(HTTPException):
    def __init__(
        self,
        message: str,
        error_code: str,
        status_code: int,
        headers: dict[str, str] | None = None,
    ):
        self.message = message
        self.error_code = error_code
        self.status_code = status_code
        super(BaseException, self).__init__(
            status_code=status_code, detail=self.__str__(), headers=headers
        )

    def __str__(self) -> str:
        return f"{self.error_code}::{self.message}"

    def __repr__(self) -> str:
        return self.__str__()


class BadRequest(BaseException):
    def __init__(
        self, message: str = "Bad Request", error_code: str = "OTH401"
    ) -> None:
        super(BadRequest, self).__init__(message, error_code, 400)


class Unauthorized(BaseException):
    def __init__(
        self, message: str = "Unauthorized", error_code: str = "OTH401"
    ) -> None:
        super(Unauthorized, self).__init__(message, error_code, 401)


class Forbidden(BaseException):
    def __init__(self, message: str = "Forbidden", error_code: str = "OTH401") -> None:
        super(Forbidden, self).__init__(message, error_code, 403)


class NotFound(BaseException):
    def __init__(self, message: str = "Not Found", error_code: str = "OTH401") -> None:
        super(NotFound, self).__init__(message, error_code, 404)


class Conflict(BaseException):
    def __init__(self, message: str = "Conflict", error_code: str = "OTH401") -> None:
        super(Conflict, self).__init__(message, error_code, 409)


class ContentTooLarge(BaseException):
    def __init__(
        self, message: str = "Content Too Large", error_code: str = "OTH401"
    ) -> None:
        super(ContentTooLarge, self).__init__(message, error_code, 413)


class UnprocessableContent(BaseException):
    def __init__(
        self, message: str = "Unprocessable Content", error_code: str = "OTH401"
    ) -> None:
        super(UnprocessableContent, self).__init__(message, error_code, 422)


class InternalServerError(BaseException):
    def __init__(
        self, message: str = "Internal Server Error", error_code: str = "OTH201"
    ) -> None:
        super(InternalServerError, self).__init__(message, error_code, 500)
