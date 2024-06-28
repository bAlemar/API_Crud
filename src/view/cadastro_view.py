from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.view.interfaces.view_interface import ViewInterface
from src.controller.interface.cadastro_controller_interface import CasdastroControleInterface
from src.validators.cadastro_validator import casdastro_validator

class CadastroView(ViewInterface):
    def __init__(self, controller: CasdastroControleInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body = http_request.body
            casdastro_validator(body)
            
            elements = body["attributes"]

            response = self.__controller.run(elements)

            return HttpResponse(status_code=200, body={ "response": response })
        # Aqui entrar nosso tratamento de error:
        except Exception as exception:
            return HttpResponse(status_code=500, body={ "error": str(exception) })
