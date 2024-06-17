from src.controller.interface.search_controller_interface import SearchControleInterface
from src.models.repositories.interface.cliente_interface import BancoDadosClienteInterface
from src.models.repositories.clientes import Usuarios_SQL
from typing import Dict

class SearchController(SearchControleInterface):
    def __init__(self, bancodados: BancoDadosClienteInterface) -> None:
        self.bancodados = bancodados
    
    def search(self, nome: str) -> Dict:
        cliente = self.bancodados.search(nome)
        cliente = self.__format_data(cliente)
        return cliente
    
    def __format_data(self, dados: Usuarios_SQL):
        dados_json = {
            "nome":dados.nome,
            "Telefone":dados.telefone,
            "Email":dados.email,
            "Endereco":dados.endereco
        }
        return dados_json