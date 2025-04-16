class FaceMismatchException(Exception):
    def __init__(self, user_id: str):
        self.client_request_token = user_id
