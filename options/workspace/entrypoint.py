from option_chain import OptionChain
from trade import Trade
from arbitrage_finder import ArbitrageFinder
from ml_model import MLModel
from option_pricing_optimizer import OptionPricingOptimizer

# Example usage
option_chain = OptionChain('AAPL')
trade = Trade('AAPL', option_chain.options[0], 'buy')
arbitrage_finder = ArbitrageFinder(option_chain)
arbitrage_finder.find_arbitrage_opportunities()
ml_model = MLModel()
ml_model.train(option_chain)
option_pricing_optimizer = OptionPricingOptimizer(option_chain)
option_pricing_optimizer.optimize_prices()
