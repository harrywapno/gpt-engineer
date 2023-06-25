from option import Option

class OptionChain:
    def __init__(self, equity):
        self.equity = equity
        self.options = self._get_options()

    def _get_options(self):
        # Code to retrieve option chain data from NYSE API
        # Returns a list of Option objects
        pass
