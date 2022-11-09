
import deta

from symbols.domain.ports.SymbolDBInterface import SymbolDBInterface
from deta import Deta


class SymbolDetaDB(SymbolDBInterface):
    db: deta.Base

    def __init__(self):
        deta_i = Deta('b0o3v2w0_fdzNh2XHgajWMzQEdz7jmj2GfwnADmVv')
        self.db = deta_i.Base('symbolsDb')

    def fetch(self, limit: int) -> [dict]:
        result = self.db.fetch(limit=limit)
        if result.count > 0:
            return result.items
        else:
            return None

    def get(self, uid: str) -> dict:
        return self.db.get(uid)

    def insert(self, symbol: dict, uid: str) -> dict:
        return self.db.put(symbol, uid)

    def update(self, symbol: dict, uid: str):
        self.db.update(symbol, uid)

    def get_by_symbol(self, symbol: str) -> dict:
        result = self.db.fetch([{"symbol": symbol}], limit=1)
        if result.count > 0:
            return result.items[0]
        return None
