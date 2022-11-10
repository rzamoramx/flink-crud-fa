
import uuid
from symbols.domain.ports.SymbolDBInterface import SymbolDBInterface
from symbols.domain.model.SymbolDomain import SymbolDomain
from symbols.domain.model.SymbolDomain import DomainSymbolModel


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
        # Generate uuid v4
        uid = str(uuid.uuid4())

        # We use a domain model logic
        symb = SymbolDomain.add_mkt_value_to_symbol(
            DomainSymbolModel(symbol["company_name"], symbol["company_description"], symbol["symbol"], symbol["market_values"])
        )
        symbol["market_values"] = symb.market_values

        # save
        self.symbol_db.insert(symbol, uid)
        return uid

    def retrieve(self, symbol_id: str) -> dict:
        result = self.symbol_db.get_by_symbol(symbol_id)
        if result is not None:
            # Replace key name
            uid = result["key"]
            del result["key"]
            result.update({"uid": uid})

        return result

    def all(self) -> [dict]:
        # Get all symbols from database, limited to 1000
        items = self.symbol_db.fetch(1000)
        if items is not None:
            for idx in range(len(items)):
                # Replace key name
                uid = items[idx]["key"]
                del items[idx]['key']
                items[idx].update({"uid": uid})

        return items

    def delete(self, symbol: str) -> bool:
        return self.symbol_db.delete_symbol(symbol)
