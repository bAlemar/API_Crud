from src.controller.update_controller import UpdateController
from src.view.update_view import UpdateView
from src.models.repositories.clientes import BancoDadosClientes


def update_composer():
    model = BancoDadosClientes()
    controller = UpdateController(model)
    view = UpdateView(controller)
    return view