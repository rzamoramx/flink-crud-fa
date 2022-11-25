
import unittest
import uuid
from symbols.adapters.postgresql.SymbolDB import SymbolPostgres
from symbols.domain.model.SymbolDomain import DomainSymbolModel


class TestSymbolDBPostgres(unittest.TestCase):
    symbol_postgres = SymbolPostgres()

    def test_delete_by_symbol(self):
        uid = str(uuid.uuid4())
        instance = DomainSymbolModel('foo', 'bar', 'NVDA', '12,34,5,6,78')
        self.symbol_postgres.insert(instance, uid)

        expected = 1
        actual = self.symbol_postgres.delete_symbol("NVDA")

        self.assertEqual(expected, actual, 'affected rows must be > 0')

    def test_fetch_all(self):
        results = self.symbol_postgres.fetch(1000)
        for symbol in results:
            print(f'symbol: {symbol}')

    def test_get_by_symbol_not_exists(self):
        result = self.symbol_postgres.get_by_symbol('FOO')
        print(f'result: {result}')

    def test_get_by_symbol(self):
        result = self.symbol_postgres.get_by_symbol('NVDA')
        print(f'result: {result}')

    def test_get_by_uid(self):
        result = self.symbol_postgres.get("e0a57070-b6b3-4301-becc-319601181b74")
        print(f'result: {result}')

    def test_insert_one(self):
        uid = str(uuid.uuid4())
        instance = DomainSymbolModel('xd', 'xd', 'APPL', '12,34,5,6,78')
        actual = self.symbol_postgres.insert(instance, uid)
        print(f'result: {actual}')

