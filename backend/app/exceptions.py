from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


async def response_validation_exception_handler(request, exc):
    error: dict = exc.errors()[0]
    # fmt: off
    message = "Validation error, since the data from database equal to: {body}"
    error["msg"] = message.format(
        body=exc.body
    )
    # fmt: on
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


class UserEmailAlreadyExist(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email is already exists",
        )


class UserNotAuthenticated(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User unauthorized, need to login to continue",
        )
