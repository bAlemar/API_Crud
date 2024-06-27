from validators.cadastro_validator import casdastro_validator


class MockRequest:
    def __init__(self) -> None:
        self.json = None

def test_cadastro_validator():
    request = MockRequest()
    request.json = {
        "attributes": {
        "nome": "Bernardo",
        "telefone": "21313123121",  # Certifique-se de que as chaves estão em minúsculas
        "email": "bernardo.alemar@htomail.com",
        "endereco": "Rua itapuca 22,402"
    }}

    casdastro_validator(request)