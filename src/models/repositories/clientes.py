import os
from src.models.repositories.infra.connections import DBConnectionHandler
from src.models.repositories.interface.cliente_interface import BancoDadosClienteInterface
from src.models.entities.usuarios import Usuarios_SQL
class BancoDadosClientes(BancoDadosClienteInterface):
    def __init__(self,) -> None:
        pass

    def insert(self,dados:Usuarios_SQL):
        """
        Cadastro de clientes
        """
        with DBConnectionHandler() as db:
            try:
                db.session.add(dados)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e

        