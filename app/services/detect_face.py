
import numpy as np
import cv2
from app.exceptions.no_face_detected_exception import NoFaceDetectedException
from app.config.config import settings

modelFile = "app/models/res10_300x300_ssd_iter_140000.caffemodel"
configFile = "app/models/deploy.prototxt"
net = cv2.dnn.readNetFromCaffe(configFile, modelFile)

def detect_face(img_bytes):
    nparr = np.frombuffer(img_bytes, np.uint8)
    
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    blob = cv2.dnn.blobFromImage(img, 1.0, (300, 300), [104, 117, 123], False, False)

    net.setInput(blob)
    detections = net.forward()
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2] * 100
        if confidence >= settings.detect_face_confidence_threshold:
            return True

    raise NoFaceDetectedException()