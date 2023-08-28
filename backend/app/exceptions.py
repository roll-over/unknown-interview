from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder


async def response_validation_exception_handler(request, exc):
    error: dict = exc.errors()[0]
    # fmt: off
    error["msg"] = "Validation error, since the data from database equal to: {body}".format(
        body=exc.body
    )
    # fmt: on
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )
