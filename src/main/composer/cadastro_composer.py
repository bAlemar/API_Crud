from src.controller.cadastro_controller import CadastroController
from src.view.cadastro_view import CadastroView
from src.models.repositories.clientes import BancoDadosClientes


def cadastro_composer():
    model = BancoDadosClientes()
    controller = CadastroController(model)
    view = CadastroView(controller)
    return view