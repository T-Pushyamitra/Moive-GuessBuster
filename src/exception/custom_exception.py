from fastapi import status

class AppError(Exception):
    """Base app exception with message + HTTP status code."""
    def __init__(self, message: str, status_code: int = status.HTTP_400_BAD_REQUEST):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class NotFoundError(AppError):
    def __init__(self, entity: str):
        super().__init__(f"{entity} not found", status_code=status.HTTP_404_NOT_FOUND)


class ConflictError(AppError):
    def __init__(self, message: str):
        super().__init__(message, status_code=status.HTTP_409_CONFLICT)

class BadRequestError(AppError):
    def __init__(self, message, status_code = status.HTTP_400_BAD_REQUEST):
        super().__init__(message, status_code)