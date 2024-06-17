from src.controller.search_controller import SearchController
from src.view.search_view import SearchView
from src.models.repositories.clientes import BancoDadosClientes


def search_composer():
    model = BancoDadosClientes()
    controller = SearchController(model)
    view = SearchView(controller)
    return view