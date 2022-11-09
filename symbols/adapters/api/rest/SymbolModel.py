
from typing import Union
from pydantic import BaseModel


class Symbol(BaseModel):
    company_name: str
    company_description: Union[str, None] = None
    symbol: str
    market_values: str
