from src.controller.delete_controller import DeleteController
from src.view.delete_view import DeleteView
from src.models.repositories.clientes import BancoDadosClientes


def delete_composer():
    model = BancoDadosClientes()
    controller = DeleteController(model)
    view = DeleteView(controller)
    return view