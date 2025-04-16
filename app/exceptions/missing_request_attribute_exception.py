class MissingRequestAttributeException(Exception):
    def __init__(self, attr: str, name: str):
        self.attr = attr
        self.name = name
