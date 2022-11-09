
from symbols.domain.ports.SymbolDBInterface import SymbolDBInterface
from symbols.config.conf import PROJECT_ID


# Firestore logic
class SymbolFirestore(SymbolDBInterface):
    def __init__(self):
        pass

    def fetch(self, limit: int) -> [dict]:
        print(f'Project id: {PROJECT_ID}')
        return []

    def get(self, uid: str) -> dict:
        pass

    def insert(self, symbol: dict, uid: str) -> dict:
        pass

    def update(self, symbol: dict, uid: str):
        pass

    def get_by_symbol(self, symbol: str) -> dict:
        pass
