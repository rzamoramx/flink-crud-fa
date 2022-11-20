import unittest
from symbols.adapters.detadb.SymbolDB import SymbolDetaDB
from symbols.domain.model.Symbol import DomainSymbolModel


class TestSymbolDBDetadb(unittest.TestCase):
    symbol_deta_db = SymbolDetaDB()

    def test_insert_one(self):
        instance = DomainSymbolModel('xd', 'xd', 'FBAR', '12,34,5,6,78')
        actual = self.symbol_deta_db.insert(instance, "")
        print(f'actual: {actual}')

    def test_fetch_all(self):
        symbols = self.symbol_deta_db.fetch(1000)
        print(f'symbols: {symbols}')

    def test_get_one(self):
        expected = {"company_name": "nvidia", "company_description": "nvidia corporation", "symbol": "NVDA", "market_values": "30,50,60,100,10", "key": "0290c10e-7557-45e9-91af-7d554a65b976"}
        actual = self.symbol_deta_db.get_by_symbol(expected["symbol"])
        self.assertEqual(expected, actual, msg="expected and actual are not equal")
