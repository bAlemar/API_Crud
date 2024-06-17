from abc import ABC, abstractmethod
from typing import Type, Dict


class UpdateControllerInterface(ABC):
    def run(self,dados_json: Dict):
        pass
