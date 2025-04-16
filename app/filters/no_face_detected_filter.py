from fastapi import Request, status
from fastapi.responses import JSONResponse
from app.exceptions.no_face_detected_exception import NoFaceDetectedException

async def no_face_detected_filter(request: Request, exc: NoFaceDetectedException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": f"No face detected"},
    )
