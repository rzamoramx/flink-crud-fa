
from abc import ABC, abstractmethod


class SymbolDBInterface(ABC):
    @abstractmethod
    def fetch(self, limit: int) -> [dict]:
        pass

    @abstractmethod
    def get(self, uid: str) -> dict:
        pass

    @abstractmethod
    def insert(self, symbol: dict, uid: str) -> dict:
        pass

    @abstractmethod
    def update(self, symbol: dict, uid: str):
        pass

    @abstractmethod
    def get_by_symbol(self, symbol: str) -> dict:
        pass
