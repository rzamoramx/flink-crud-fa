
from symbols.domain.ports.SymbolsMessageBrokerInterface import SymbolsMessageBrokerInterface
from symbols.config.conf import PROJECT_ID


# GCP pubsub logic
class SymbolsPubsub(SymbolsMessageBrokerInterface):
    def __init__(self):
        pass

    def publish(self, message: dict) -> Exception:
        # Your logic to send message here
        print(f'Project id: {PROJECT_ID}')
        return None
