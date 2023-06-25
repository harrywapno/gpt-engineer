from typing import List
from option import Option
from equity import Equity

class Portfolio:
    def __init__(self, options: List[Option], equities: List[Equity]):
        self.options = options
        self.equities = equities

    def add_option(self, option: Option):
        self.options.append(option)

    def add_equity(self, equity: Equity):
        self.equities.append(equity)

    def remove_option(self, option: Option):
        self.options.remove(option)

    def remove_equity(self, equity: Equity):
        self.equities.remove(equity)

    def calculate_value(self) -> float:
        # TODO: implement calculation of portfolio value
        return 0.0
