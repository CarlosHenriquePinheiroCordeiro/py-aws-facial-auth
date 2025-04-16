from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.file_size_not_allowed_exception import FileSizeNotAllowedException

async def file_size_not_allowed_filter(request: Request, exc: FileSizeNotAllowedException):
    return JSONResponse(
        status_code=409,
        content={"message": f"File size ({exc.file_size}MB) not allowed for {exc.client_request_token}, it is greater than 10MB."},
    )
