from fastapi import FastAPI

from app.router import router
from app.config.tracer import trace_app
from app.exceptions.missing_request_attribute_exception import MissingRequestAttributeException
from app.exceptions.no_face_detected_exception import NoFaceDetectedException
from app.exceptions.face_mismatch_exception import FaceMismatchException
from app.filters.missing_request_attribute_filter import missing_request_attribute_filter
from app.filters.no_face_detected_filter import no_face_detected_filter
from app.filters.face_mismatch_filter import face_mismatch_filter

app = FastAPI(
    title="Face API",
    version="1.0.0",
)

trace_app(app)

app.add_exception_handler(MissingRequestAttributeException, missing_request_attribute_filter)
app.add_exception_handler(NoFaceDetectedException, no_face_detected_filter)
app.add_exception_handler(FaceMismatchException, face_mismatch_filter)

app.include_router(router.router)
