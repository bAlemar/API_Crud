from src.controller.interface.search_controller_interface import SearchControleInterface
from src.models.repositories.interface.cliente_interface import BancoDadosClienteInterface
from src.models.repositories.clientes import Usuarios_SQL
from typing import Dict

class DeleteController(SearchControleInterface):
    def __init__(self, bancodados: BancoDadosClienteInterface) -> None:
        self.bancodados = bancodados
    
    def delete(self, nome: str) -> Dict:
        cliente = self.bancodados.delete(nome)
    
        return f"Usuario {nome} excluido com sucesso"
    
    