from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.no_human_authentication_exception import NoHumanAuthenticationException

async def no_human_authentication_filter(request: Request, exc: NoHumanAuthenticationException):
    return JSONResponse(
        status_code=409,
        content={"message": f"Authentication attempt for {exc.client_request_token} not sent from a human."},
    )
