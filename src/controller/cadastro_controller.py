from src.controller.interface.cadastro_controller_interface import CasdastroControleInterface
from src.models.repositories.interface.cliente_interface import BancoDadosClienteInterface
from src.models.entities.usuarios import Usuarios_SQL
from typing import Dict

class CadastroController(CasdastroControleInterface):
    def __init__(self, bancodados: BancoDadosClienteInterface) -> None:
        self.bancodados = bancodados
    
    def run(self,dados_json: Dict):
        print('dados_json',dados_json)
        
        dados = self.__format_dados(dados_json)
        
        print('dados',dados)
        
        self.__cadastro_cliente(dados)
        return 'COMPLETADO'
    
    def __format_dados(self,dados_json):    
        usuarios_data = Usuarios_SQL(
            nome = dados_json["nome"],
            telefone = dados_json["telefone"],
            email = dados_json["email"],
            endereco = dados_json["endereco"]
        )
        return usuarios_data
        
    def __cadastro_cliente(self,dados:Usuarios_SQL):
        self.bancodados.insert(dados)
        
    
    