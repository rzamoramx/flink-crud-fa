
from symbols.domain.ports.SymbolDBInterface import SymbolDBInterface
from symbols.config.conf import SOME_ENV_VAR


# Firestore logic
class SymbolFirestore(SymbolDBInterface):
    def __init__(self):
        pass

    def fetch(self, limit: int) -> [dict]:
        print(f'some env var: {SOME_ENV_VAR}')
        return []

    def get(self, uid: str) -> dict:
        pass

    def insert(self, symbol: dict, uid: str) -> dict:
        pass

    def update(self, symbol: dict, uid: str):
        pass

    def get_by_symbol(self, symbol: str) -> dict:
        pass

    def delete_symbol(self, symbol: str) -> bool:
        pass
