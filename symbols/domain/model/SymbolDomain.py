

class SymbolDomain:
    def __init__(self):
        pass

    @staticmethod
    def calc_rate(client_id: str, pre_rate: float) -> (float, Exception):
        # Domain model logic here
        if client_id == "cargamos":
            rate = 20 * 2 + pre_rate
        else:
            rate = 200.00

        return rate, None
