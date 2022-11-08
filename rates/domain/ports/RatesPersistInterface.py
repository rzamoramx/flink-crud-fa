
from abc import ABC, abstractmethod


class RatesPersistInterface(ABC):
    @abstractmethod
    def get_by_id(self, rate_id: str) -> (dict, Exception):
        pass
