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

    def search(self,nome:str):
        """
        Search na tabela clientes por nome
        """
        with DBConnectionHandler() as db:
            try:
                cliente = db.session.query(Usuarios_SQL).filter_by(nome=nome).first()
                return cliente
            except Exception as e:
                db.session.rollback()
                raise e
    def delete(self,nome:str):
        """
        Deleta um usuario pelo nome.
        Exclui mesmo se o usuário não existe, verificar isso...
        """
        with DBConnectionHandler() as db:
            try:
                delete = db.session.query(Usuarios_SQL).filter_by(nome=nome).delete()
                db.session.commit()
                return delete

            except Exception as e:
                db.session.rollback()
                raise e
    def update(self,dados:Usuarios_SQL):
        """
        Faz update dos dados a partir do nome
        """
        # Preciso do json atual e json para att
        with DBConnectionHandler() as db:
            try:
                nome = dados["nome"]
                update = db.session \
                .query(Usuarios_SQL) \
                .filter_by(nome=nome) \
                .update(dados)
                
                db.session.commit()
                return update
            
            except Exception as e:
                db.session.rollback()
                raise e
