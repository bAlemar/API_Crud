from abc import ABC, abstractmethod
from typing import Type, Dict


class DeleteControleInterface(ABC):
    def delete(self,nome: str):
        pass
