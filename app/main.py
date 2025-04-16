from fastapi import FastAPI

from app.router import router
from app.config.tracer import trace_app
from app.exceptions.missing_request_attribute_exception import MissingRequestAttributeException
from app.exceptions.file_size_not_allowed_exception import FileSizeNotAllowedException
from app.exceptions.no_face_detected_exception import NoFaceDetectedException
from app.exceptions.face_mismatch_exception import FaceMismatchException
from app.exceptions.no_human_authentication_exception import NoHumanAuthenticationException
from app.filters.missing_request_attribute_filter import missing_request_attribute_filter
from app.filters.file_size_not_allowed_filter import file_size_not_allowed_filter
from app.filters.no_face_detected_filter import no_face_detected_filter
from app.filters.face_mismatch_filter import face_mismatch_filter
from app.filters.no_human_authentication_filter import no_human_authentication_filter

app = FastAPI(
    title="Face API",
    version="1.0.0",
)

trace_app(app)

app.add_exception_handler(MissingRequestAttributeException, missing_request_attribute_filter)
app.add_exception_handler(FileSizeNotAllowedException, file_size_not_allowed_filter)
app.add_exception_handler(NoFaceDetectedException, no_face_detected_filter)
app.add_exception_handler(FaceMismatchException, face_mismatch_filter)
app.add_exception_handler(NoHumanAuthenticationException, no_human_authentication_filter)

app.include_router(router.router)
