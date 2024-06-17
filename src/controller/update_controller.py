from src.controller.interface.update_controller_interface import UpdateControllerInterface
from src.models.repositories.interface.cliente_interface import BancoDadosClienteInterface
from typing import Dict

class UpdateController(UpdateControllerInterface):
    def __init__(self,bancodados: BancoDadosClienteInterface) -> None:
        self.bancodados = bancodados
        return

    def run(self,dados_json:Dict):
        result = self.__update_data(dados_json)
        return result

    def __update_data(self,dados_json:Dict):
        return self.bancodados.update(dados_json)