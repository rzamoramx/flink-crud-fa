import unittest
from symbols.domain.SymbolsApp import SymbolsApp
from symbols.adapters.detadb.SymbolDB import SymbolDetaDB


class TestSymbolsApp(unittest.TestCase):
    symbol_app = SymbolsApp(SymbolDetaDB())

    def test_retrieve_when_not_exists(self):
        symbol_id = "NOTEXISTS"
        symbol = self.symbol_app.retrieve(symbol_id)
        self.assertIsNone(symbol, msg="symbol are not None")

    def test_retrieve_ok(self):
        symbol_id = "NVDA"
        symbol = self.symbol_app.retrieve(symbol_id)
        self.assertEqual(symbol['symbol'], symbol_id, msg="symbols id are not equal")
