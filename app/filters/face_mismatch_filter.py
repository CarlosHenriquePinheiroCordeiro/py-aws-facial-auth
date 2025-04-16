from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.face_mismatch_exception import FaceMismatchException

async def face_mismatch_filter(request: Request, exc: FaceMismatchException):
    return JSONResponse(
        status_code=409,
        content={"message": f"Face mismatch for {exc.user_id}."},
    )
