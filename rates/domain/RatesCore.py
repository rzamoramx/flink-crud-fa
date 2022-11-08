
import random
import string
from rates.domain.ports.RatesPersistInterface import RatesPersistInterface
from rates.domain.ports.RatesMessageBrokerInterface import RatesMessageBrokerInterface
from rates.domain.model.Rates import Rates


class RatesCore:
    rates_persist: RatesPersistInterface = None
    rates_message_broker: RatesMessageBrokerInterface = None

    def __init__(self, rp, rmb):
        if rp is None:
            raise Exception("an instance of rates persist is required")

        if rmb is None:
            raise Exception("an instance of rates message broker is required")

        self.rates_persist = rp
        self.rates_message_broker = rmb

    def process_rate(self, rate_id: str) -> (float, Exception):
        # Get rate from database
        pre_rate, err = self.rates_persist.get_by_id(rate_id)

        # Use domain model logic
        rate, err = Rates.calc_rate("cargamos", pre_rate["rate"])

        # Publish rate
        if err is None:
            rid = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
            err = self.rates_message_broker.publish({"rate": rate, "id": rid})

        # Return result
        if err is None:
            return rate, None
        else:
            return 00.00, Exception("Exception occurred: " + str(err))
