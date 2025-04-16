from fastapi import Request, status
from fastapi.responses import JSONResponse
from app.exceptions.face_mismatch_exception import FaceMismatchException

async def face_mismatch_filter(request: Request, exc: FaceMismatchException):
    return JSONResponse(
        status_code=status.HTTP_406_NOT_ACCEPTABLE,
        content={"message": f"Face mismatch for {exc.user_id}."},
    )
