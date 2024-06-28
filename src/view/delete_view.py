from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.view.interfaces.view_interface import ViewInterface
from src.controller.interface.delete_controller_interface import DeleteControleInterface
from src.errors.error_handler import handle_erros
from src.validators.search_validator import search_validator

class DeleteView(ViewInterface):
    def __init__(self, controller: DeleteControleInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body = http_request.body
            search_validator(body)
            element = body["nome"]

            response = self.__controller.delete(element)

            return HttpResponse(status_code=200, body={ "response": response })
        except Exception as exception:
            return handle_erros(exception)
