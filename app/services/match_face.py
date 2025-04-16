from botocore.exceptions import ClientError
from app.config.rekognition import rekognition
from app.config.config import settings
from app.exceptions.face_mismatch_exception import FaceMismatchException

def match_face(user_id, img_bytes):
    try:
        response = rekognition.compare_faces(
            SourceImage={
                'Bytes': img_bytes
            },
            TargetImage={
                'S3Object': {
                    'Bucket': settings.s3_upload_face_bucket_name,
                    'Name': (f"{user_id}.jpg")
                }
            },
            SimilarityThreshold=settings.face_match_confidence_threshold
        )
        print(response)
        face_matches = response['FaceMatches']
        if (len(face_matches) > 0):
            if (face_matches[0]['Similarity'] >= settings.face_match_confidence_threshold):
                return True
        raise FaceMismatchException(user_id)
    except ClientError as error:
        print(error)
        return False