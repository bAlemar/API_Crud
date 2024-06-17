from abc import ABC, abstractmethod

class BancoDadosClienteInterface(ABC):
    @abstractmethod
    def insert(self,data):
        pass