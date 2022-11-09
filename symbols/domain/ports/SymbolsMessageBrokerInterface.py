
from abc import ABC, abstractmethod


class SymbolsMessageBrokerInterface(ABC):
    @abstractmethod
    def publish(self, message: dict) -> Exception:
        pass
