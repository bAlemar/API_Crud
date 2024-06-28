from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.view.interfaces.view_interface import ViewInterface
from src.controller.interface.update_controller_interface import UpdateControllerInterface
from src.validators.cadastro_validator import casdastro_validator
from src.errors.error_handler import handle_erros

class UpdateView(ViewInterface):
    def __init__(self, controller: UpdateControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body = http_request.body
            casdastro_validator(body)
            element = body["attributes"]
            response = self.__controller.run(element)
            return HttpResponse(status_code=200, body={ "response": response })
        except Exception as exception:
            return handle_erros(exception)
