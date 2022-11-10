
from symbols.domain.ports.SymbolsMessageBrokerInterface import SymbolsMessageBrokerInterface
from symbols.config.conf import SOME_ENV_VAR


# GCP pubsub logic
class SymbolsPubsub(SymbolsMessageBrokerInterface):
    def __init__(self):
        pass

    def publish(self, message: dict) -> Exception:
        # Your logic to send message here
        print(f'Project SOME_ENV_VAR: {SOME_ENV_VAR}')
        return None
