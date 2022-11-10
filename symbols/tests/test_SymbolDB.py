import unittest
from symbols.adapters.detadb.SymbolDB import SymbolDetaDB


class TestSymbolDB(unittest.TestCase):
    symbol_deta_db = SymbolDetaDB()

    def test_fetch_all(self):
        pass

    def test_get_one(self):
        expected = {"company_name": "nvidia", "company_description": "nvidia corporation", "symbol": "NVDA", "market_values": "30,50,60,100,10", "key": "0290c10e-7557-45e9-91af-7d554a65b976"}
        actual = self.symbol_deta_db.get_by_symbol(expected["symbol"])
        self.assertEqual(expected, actual, msg="expected and actual are not equal")
