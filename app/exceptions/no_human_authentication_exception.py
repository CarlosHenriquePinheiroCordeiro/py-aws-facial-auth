class NoHumanAuthenticationException(Exception):
    def __init__(self, client_request_token: str):
        self.client_request_token = client_request_token
