from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.missing_request_attribute_exception import MissingRequestAttributeException

async def missing_request_attribute_filter(request: Request, exc: MissingRequestAttributeException):
    return JSONResponse(
        status_code=409,
        content={"message": f"Missing {exc.attr} {exc.name}"},
    )
