from fastapi import APIRouter, File, UploadFile, Form
from app.middlewares.verify_request_middleware import VerifyRequestMiddleware
from app.services.upload_face import upload_face
from app.services.detect_face import detect_face
from app.services.match_face import match_face
from app.services.create_liveness_check_session import create_liveness_check_session
from app.tracing.trace_process import trace_process

router = APIRouter(
    prefix="/facial-auth",
    tags=["Facial Authentication"],
    #route_class=VerifyRequestMiddleware
)

@router.post("/insert-face")
async def insert_face(
    face_img: UploadFile = File(...),
    user_id: str = Form(...)
):
    face_bytes = await face_img.read()
    detect_face(face_bytes)
    upload_face(user_id)
    return {"message": "Face insertion successful!"}

@router.post("/start-auth-face")
async def auth_face(
    face_img: UploadFile = File(...),
    user_id: str = Form(...),
    client_request_token: str = Form(...)
):
    face_bytes = await face_img.read()
    detect_face(face_bytes)
    match_face(user_id, face_bytes)
    session_id = create_liveness_check_session(client_request_token)
    return {"message": "Authentication session started successfully! See session_id!", "session_id": session_id}
    

@router.put("/update-face")
async def update_face(
    face_img: UploadFile = File(...),
    user_id: str = Form(...)
):
    face_bytes = await face_img.read()
    detect_face(face_bytes)
    upload_face(user_id)
    return {"message": "Face updated successfully!"}