
from typing import List
from fastapi import Depends, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from symbols.domain.SymbolsApp import SymbolsApp
#from symbols.adapters.detadb.SymbolDB import SymbolDetaDB as DB
from symbols.adapters.postgresql.SymbolDB import SymbolPostgres as DB
from symbols.adapters.api.rest.SymbolModel import Symbol

router = InferringRouter()


# wire up
def inject_symbols_app_dep():
    # Here you choose what implementations you will need and inject to app
    return SymbolsApp(DB())


@cbv(router)
class V1:
    symbols_app: SymbolsApp = Depends(inject_symbols_app_dep)

    @router.put("/symbol")
    def update_symbol(self, symb: Symbol):
        """Update symbol
        :param symb: Symbol model instance
        payload
        {
            "company_description": "apple inc",
            "company_name": "apple",
            "market_values": "20,40,60,10,98",
            "symbol": "appl"
        }
        """
        self.checks()

        try:
            self.symbols_app.update(symb.__dict__)
            return {"status": "ok", "message": "symbol updated correctly"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @router.post("/symbol")
    def post_symbol(self, symb: Symbol):
        """
        Create new symbol, the UID is autogenerated and returned in response
        :param symb: Symbol model instance
        payload
        {
            "company_description": "apple inc",
            "company_name": "apple",
            "market_values": "20,40,60,10,98",
            "symbol": "appl"
        }
        """
        self.checks()

        try:
            uid = self.symbols_app.create(symb.__dict__)
            return {"status": "ok", "uid": uid}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @router.get("/symbol/{symbol_id}", response_model=Symbol)
    def get_symbol(self, symbol_id):
        self.checks()

        symbol = self.symbols_app.retrieve(symbol_id)
        if symbol is not None:
            return {"status": "ok", "symbol": symbol}
        else:
            raise HTTPException(status_code=404, detail="symbol not found")

    @router.get("/symbol", status_code=200, response_model=List[Symbol])
    def get_symbols(self):
        """
        Get list of symbols
        :return: all symbols in DB
        """
        self.checks()

        symbols = self.symbols_app.all()
        if len(symbols) > 0:
            return {"status": "ok", "symbols": symbols}
        else:
            raise HTTPException(status_code=404, detail="symbols not found")

    @router.delete("/symbol/{symbol_id}")
    def delete_symbol(self, symbol_id):
        """
        Delete symbol
        """
        self.checks()

        ok = self.symbols_app.delete(symbol_id)
        if ok:
            return {"status": "ok", "message": "ok symbol deleted"}
        else:
            raise HTTPException(status_code=500, detail="symbols not found or cannot delete, try later")

    def checks(self):
        """
        Check required dependencies
        """
        if self.symbols_app is None:
            raise Exception("symbol app instance is required")
