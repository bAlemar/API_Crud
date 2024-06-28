from validators.search_validator import search_validator


class MockRequest:
    def __init__(self) -> None:
        self.json = None

def test_search_validator():
    request = MockRequest()
    request.json = {
        "nome":123213
        }

    search_validator(request)