from fastapi import Request, status
from fastapi.responses import JSONResponse
from app.exceptions.missing_request_attribute_exception import MissingRequestAttributeException

async def missing_request_attribute_filter(request: Request, exc: MissingRequestAttributeException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": f"Missing {exc.attr} {exc.name}"},
    )
