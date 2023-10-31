from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


async def response_validation_exception_handler(request, exc):
    if exc.body is None:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(None),
        )

    message = f"Validation error. Data from database equal to: {exc.body}"

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"error": message}),
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


class CheckUserAuthorization(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Check user authorization",
        )


class ForbiddenAction(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No permissions for this action",
        )


class InvalidRelationAction(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not possible to change relation to own records",
        )


class UserRoleMismatch(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user role does not match the record or action type",
        )
        
class RelatedRecordDoesNotExists(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Related to this action record does not exists in DB."
        )
