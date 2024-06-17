from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuarios_SQL(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer,primary_key=True)
    nome = Column(String(50),nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))

    def __repr__(self):
        return f"Nome [nome={self.nome},Telefone={self.telefone}],Email={self.email},Endereco={self.endereco}"
    




# class Usuarios:
#     def __init__(self,
#                  nome: str = None,
#                  idade: int = None,
#                  bairro: str = None,
#                  profissao: str = None
#                  ) -> None:
#         self.nome = nome
#         self.idade = idade
#         self.bairro = bairro
#         self.profissao = profissao
#         pass
