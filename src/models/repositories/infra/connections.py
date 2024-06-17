import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:

    def __init__(self) -> None:
        """
        Configurando conexão com o banco e criando o 'motor' do banco de dados.
        """
        self.__connection_string = 'postgresql://airflow:airflow@localhost:5432/postgres'
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        """
        Criação do Motor do Banco de Dados
        """
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        """
        Inicia uma sessão no banco de dados.
        Utilizado para gerenciar contexto do 'with'
        """
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
    
    def create_tables(self):
        from src.models.entities.usuarios import Usuarios_SQL
        Usuarios_SQL.__table__.create(bind=self.__engine, checkfirst=True)