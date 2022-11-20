
from symbols.domain.model.Symbol import DomainSymbolModel


# Domain model logic here, not related to DB rather related to business logic
class SymbolDomain:
    @staticmethod
    def add_mkt_value_to_symbol(symbol: DomainSymbolModel) -> DomainSymbolModel:
        """
        return market_values affected by additional value, this actually no make sense, is only for test
        :param symbol: DomainSymbolModel instance
        :return: symbol affected
        """
        if symbol.symbol == 'appl':
            symbol.market_values = symbol.market_values + ',30'
            return symbol

        symbol.market_values = symbol.market_values + ',10'
        return symbol
