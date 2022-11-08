
from rates.domain.ports.RatesPersistInterface import RatesPersistInterface
from rates.config.conf import PROJECT_ID


# Firestore logic
class RatesPersist(RatesPersistInterface):
    def __init__(self):
        pass

    def get_by_id(self, rate_id: str) -> (dict, Exception):
        # Your logic to retrieve data from firestore here
        print(f'Project id: {PROJECT_ID}')
        return {"id": "1234", "rate": 89.00}, None
