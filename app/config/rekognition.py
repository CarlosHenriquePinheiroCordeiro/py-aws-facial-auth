import boto3
from app.config.config import settings

rekognition = boto3.client(
    'rekognition',
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key,
    region_name=settings.aws_region_name
)