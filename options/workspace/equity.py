from dataclasses import dataclass

@dataclass
class Equity:
    ticker_symbol: str
    current_price: float
