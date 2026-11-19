from http import HTTPStatus

from ninja.errors import HttpError


def success_response(message: str, data=None):
    """
    Standard success response.
    """

    return {
        "status": True,
        "message": message,
        "data": data,
    }


def error_response(message: str):
    """
    Standard error response.
    """

    return {
        "status": False,
        "message": message,
    }


def raise_not_found(message="Resource not found."):
    """
    Raise 404 Not Found.
    """

    raise HttpError(
        HTTPStatus.NOT_FOUND,
        message,
    )


def raise_validation_error(message):
    """
    Raise 422 Validation Error.
    """

    raise HttpError(
        HTTPStatus.UNPROCESSABLE_ENTITY,
        message,
    )


def raise_server_error(message="Internal server error."):
    """
    Raise 500 Server Error.
    """

    raise HttpError(
        HTTPStatus.INTERNAL_SERVER_ERROR,
        message,
    )