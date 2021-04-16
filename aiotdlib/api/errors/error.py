class AioTDLibError(Exception):
    """This is the base exception class for all TDLib API related errors."""
    code: int = None
    message: str = None

    def __init__(self, code: int, message: str):
        super().__init__(message)
        self.code = code
        self.message = message

    def __str__(self) -> str:
        return f"[Error {self.code}] {self.message}"


class BadRequest(AioTDLibError):
    def __init__(self, message: str):
        super(BadRequest, self).__init__(400, message)


class Unauthorized(AioTDLibError):
    def __init__(self, message: str):
        super(Unauthorized, self).__init__(401, message)
