
from rates.domain.ports.RatesMessageBrokerInterface import RatesMessageBrokerInterface
from rates.config.conf import PROJECT_ID


# GCP pubsub logic
class RatesMessageBroker(RatesMessageBrokerInterface):
    def __init__(self):
        pass

    def publish(self, message: dict) -> Exception:
        # Your logic to send message here
        print(f'Project id: {PROJECT_ID}')
        return None
