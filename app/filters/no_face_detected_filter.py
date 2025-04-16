from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.no_face_detected_exception import NoFaceDetectedException

async def no_face_detected_filter(request: Request, exc: NoFaceDetectedException):
    return JSONResponse(
        status_code=409,
        content={"message": f"No face detected"},
    )
