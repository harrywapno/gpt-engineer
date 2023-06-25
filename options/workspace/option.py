from dataclasses import dataclass
from typing import Union

@dataclass
class Option:
    strike_price: float
    expiration_date: str
    option_type: str

    def get_price(self):
        # Code to retrieve option price from NYSE API
        pass
