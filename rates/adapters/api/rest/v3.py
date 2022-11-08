
from fastapi import Depends, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from rates.domain.RatesCore import RatesCore
import __main__

router = InferringRouter()


def inject_rate_core_dep():
    return __main__.api.__getattribute__("rates_app")


@cbv(router)
class V3:
    rates_core: RatesCore = Depends(inject_rate_core_dep)

    @router.get("/rate", status_code=201)
    def get_rate(self):
        self.checks()

        rate, err = self.rates_core.process_rate("1234")

        if err is None:
            return {"status": "ok", "rate": rate}
        else:
            print(f'error on processing rate: {err}')
            raise HTTPException(status_code=500, detail="cannot get rate")

    def checks(self):
        if self.rates_core is None:
            raise Exception("rates core instance is required")
