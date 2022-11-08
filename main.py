
from fastapi import FastAPI
from rates.adapters.api.rest.v3 import router as router_v3
from rates.domain.RatesCore import RatesCore
from rates.adapters.firestore.RatesPersist import RatesPersist as FirestoreEngine
from rates.adapters.pubsub.RatesMessageBroker import RatesMessageBroker as PubsubEngine
import uvicorn

api = FastAPI()


def main():
    wire_up()
    api.include_router(router_v3, prefix="/v3")

    @api.get("/")
    def index():
        return "ok"

    uvicorn.run(api, host="127.0.0.1", port=8081)


# Here you choose what implementations you will need
def wire_up():
    api.__setattr__("rates_app", RatesCore(FirestoreEngine(), PubsubEngine()))


if __name__ == "__main__":
    main()
