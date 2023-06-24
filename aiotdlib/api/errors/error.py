from http import HTTPStatus


class AioTDLibError(Exception):
    """This is the base exception class for all TDLib API related errors."""

    code: int = None
    message: str = None

    def __init__(self, code: int, message: str = "Unknown Error"):
        super().__init__(message)
        self.code = code
        self.message = message

    def __str__(self) -> str:
        return f"[Error {self.code}] {self.message}"


class BadRequest(AioTDLibError):
    def __init__(self, code: int = HTTPStatus.NOT_FOUND, message: str = "Bad request"):
        super(BadRequest, self).__init__(code, message)


class Unauthorized(AioTDLibError):
    def __init__(self, code: int = HTTPStatus.NOT_FOUND, message: str = "Unauthorized"):
        super(Unauthorized, self).__init__(code, message)


class NotFound(AioTDLibError):
    def __init__(self, code: int = HTTPStatus.NOT_FOUND, message: str = "Not found"):
        super(NotFound, self).__init__(code, message)


http_code_to_error = {
    HTTPStatus.BAD_REQUEST: BadRequest,
    HTTPStatus.UNAUTHORIZED: Unauthorized,
    HTTPStatus.NOT_FOUND: NotFound,
}
