class Http400Error(Exception):
    """
    Esse error é para quando cliente insere dados errados ou até url inexistentes
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'BadRequest'
        self.status_code = 400
    
    