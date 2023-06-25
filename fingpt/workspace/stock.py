from dataclasses import dataclass
from typing import List
from black_scholes import calculate_black_scholes

@dataclass
class Option:
    last: float
    ask: float
    bid: float
    volume: int
    implied_volatility: float
    # Other option data as needed

class Stock:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.option_chain = []

    def add_option_chain(self, option_chain: List[Option]):
        self.option_chain = option_chain

    def calculate_black_scholes(self, calculate_black_scholes_func):
        for option in self.option_chain:
            option.black_scholes = calculate_black_scholes_func(option)
