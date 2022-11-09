
from fastapi import Depends, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from symbols.domain.SymbolsApp import SymbolsApp
from symbols.adapters.detadb.SymbolDB import SymbolDetaDB as DetaDB
from symbols.adapters.api.rest.SymbolModel import Symbol

router = InferringRouter()


def inject_symbols_app_dep():
    # wire up
    # Here you choose what implementations you will need
    return SymbolsApp(DetaDB())


@cbv(router)
class V1:
    symbols_app: SymbolsApp = Depends(inject_symbols_app_dep)

    @router.put("/symbol")
    def delete_symbol(self, symb: Symbol):
        self.checks()

        try:
            uid = self.symbols_app.update(symb.__dict__)
            return {"status": "ok", "symbol": uid}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @router.post("/symbol")
    def post_symbol(self, symb: Symbol):
        self.checks()

        try:
            uid = self.symbols_app.create(symb.__dict__)
            return {"status": "ok", "uid": uid}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @router.get("/symbol/{symbol_id}")
    def get_symbol(self, symbol_id):
        self.checks()

        symbol = self.symbols_app.retrieve(symbol_id)
        if symbol is not None:
            return {"status": "ok", "symbol": symbol}
        else:
            raise HTTPException(status_code=404, detail="symbol not found")

    @router.get("/symbol", status_code=200)
    def get_symbols(self):
        self.checks()

        symbols = self.symbols_app.all()

        if len(symbols) > 0:
            return {"status": "ok", "symbols": symbols}
        else:
            raise HTTPException(status_code=404, detail="symbols not found")

    def checks(self):
        if self.symbols_app is None:
            raise Exception("symbol app instance is required")
