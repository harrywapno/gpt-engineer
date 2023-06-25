from option import Option

class Trade:
    def __init__(self, equity, option, trade_type):
        self.equity = equity
        self.option = option
        self.trade_type = trade_type

    def execute_trade(self):
        # Code to execute trade using NYSE API
        pass
