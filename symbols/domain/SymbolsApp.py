
import uuid
from symbols.domain.ports.SymbolDBInterface import SymbolDBInterface
from symbols.domain.model.SymbolDomain import SymbolDomain


class SymbolsApp:
    symbol_db: SymbolDBInterface = None

    def __init__(self, sdb):
        if sdb is None:
            raise Exception("an instance of symbol db is required")

        self.symbol_db = sdb

    def update(self, symbol: dict):
        symb = self.symbol_db.get_by_symbol(symbol["symbol"])
        if symb is not None:
            self.symbol_db.update(symbol, symb[0]['key'])
        else:
            raise Exception("symbol not found")

    def create(self, symbol: dict) -> str:
        id = str(uuid.uuid4())
        self.symbol_db.insert(symbol, id)
        return id

    def retrieve(self, symbol_id: str) -> dict:
        result = self.symbol_db.get_by_symbol(symbol_id)
        if result is not None:
            uid = result["key"]
            del result["key"]
            result.update({"uid": uid})

        return result

    def all(self) -> [dict]:
        # Get all symbols from database
        items = self.symbol_db.fetch(1000)
        if items is not None:
            for idx in range(len(items)):
                uid = items[idx]["key"]
                del items[idx]['key']
                items[idx].update({"uid": uid})

        return items
