from app.config.s3_client import s3_client
from botocore.exceptions import ClientError
from app.config.config import settings

def upload_face(file, user_id: str):
    try:
        s3_client.put_object(
            Bucket=settings.s3_upload_face_bucket_name,
            Key=(f"{user_id}.jpg"),
            Body=file,
            ContentType='image/jpeg',
            ContentDisposition='inline'
        )
        return True
    except ClientError as error:
        print(error)
        return False