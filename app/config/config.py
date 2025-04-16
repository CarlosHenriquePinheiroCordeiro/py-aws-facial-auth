from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_region_name: str
    s3_upload_face_bucket_name: str
    max_file_size: int
    app_env: str
    jaeger_host: str
    jaeger_port: str
    detect_face_confidence_threshold: int
    face_match_confidence_threshold: int

    class Config:
        env_file = ".env"

settings = Settings()
