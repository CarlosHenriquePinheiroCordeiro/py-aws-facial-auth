from fastapi import APIRouter, File, UploadFile, Form, status
from fastapi.responses import JSONResponse
from app.middlewares.verify_request_middleware import VerifyRequestMiddleware
from app.services.detect_face import detect_face
from app.services.match_face import match_face
from app.services.create_liveness_check_session import create_liveness_check_session
from app.tracing.trace_process import trace_process

router = APIRouter(
    prefix="/facial-auth",
    tags=["Facial Authentication"],
    #route_class=VerifyRequestMiddleware PARA USO FUTURO CASO SE ENCONTRE ALGUMA NECESSIDADE DE UTILIZAR UM MIDDLEWARE DE VALIDAÇÃO DE CORPO DA REQUISIÇÃO
)

@router.post("/face-match")
async def face_match(
    user_id: str = Form(...),
    face_img: UploadFile = File(...),
):
    default_attributes = {"face_img": str(face_img), "user_id": user_id}
    face_bytes = await trace_process('read-face-img-bytes', face_img.read, attributes=default_attributes)
    await trace_process('detect_face', detect_face, face_bytes, attributes=default_attributes)
    await trace_process('match_face_tracing', match_face, user_id, face_bytes, attributes=default_attributes)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Face match successfuly!"}
    )

@router.post("/start-liveness-session")
async def start_liveness_session(
    client_request_token: str = Form(...)
):
    default_attributes = {"client_request_token": client_request_token}
    session_id = await trace_process('create_liveness_check_session', create_liveness_check_session, client_request_token, attributes=default_attributes)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Authentication session started successfully! See session_id!", "session_id": session_id}
    )
    