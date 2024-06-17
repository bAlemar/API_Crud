from abc import ABC, abstractmethod
from typing import Type, Dict


class SearchControleInterface(ABC):
    def search(self,nome: str):
        pass
