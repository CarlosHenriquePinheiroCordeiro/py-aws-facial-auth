from app.config.rekognition import liveness_rekognition
from botocore.exceptions import ClientError

def create_liveness_check_session(request_token):
    try:
        response = liveness_rekognition.create_face_liveness_session(
            ClientRequestToken=f"{request_token}"
        )

        session_id = response['SessionId']
        return session_id
    except ClientError as error:
        print(error)
        return False