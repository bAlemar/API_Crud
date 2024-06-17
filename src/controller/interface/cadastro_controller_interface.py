from abc import ABC, abstractmethod
from typing import Type, Dict


class CasdastroControleInterface(ABC):
    def run(self,dados_json: Dict):
        pass
