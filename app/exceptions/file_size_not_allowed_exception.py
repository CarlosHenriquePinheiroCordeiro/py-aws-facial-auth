class FileSizeNotAllowedException(Exception):
    def __init__(self, client_request_token: str, file_size: int):
        self.client_request_token = client_request_token
        self.file_size = file_size
