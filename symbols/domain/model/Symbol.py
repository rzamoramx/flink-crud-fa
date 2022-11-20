
class DomainSymbolModel(object):
    company_name: str
    company_description: str
    symbol: str
    market_values: str

    def __init__(self, company_name, company_desc, symbol, market_values):
        self.company_name = company_name
        self.company_description = company_desc
        self.symbol = symbol
        self.market_values = market_values

    def items(self):
        return self.__dict__.items()
