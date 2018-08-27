

class Response:
    def __init__(self):
        self.code = 1000
        self.data = None
        self.errors = None

    @property
    def dict(self):
        return self.__dict__