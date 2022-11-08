
from abc import ABC, abstractmethod


class RatesMessageBrokerInterface(ABC):
    @abstractmethod
    def publish(self, message: dict) -> Exception:
        pass
