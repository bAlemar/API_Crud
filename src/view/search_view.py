from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.view.interfaces.view_interface import ViewInterface
from src.controller.interface.search_controller_interface import SearchControleInterface


class SearchView(ViewInterface):
    def __init__(self, controller: SearchControleInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body = http_request.body
            element = body["nome"]

            response = self.__controller.search(element)

            return HttpResponse(status_code=200, body={ "response": response })
        except Exception as exception:
            return HttpResponse(status_code=500, body={ "error": str(exception) })
