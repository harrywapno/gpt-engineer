from option import Option
from equity import Equity
from portfolio import Portfolio
from trade import Trade
from database import Database
from optimization import calculate_option_price
from machine_learning import improve_recommendations
from frontend import app

# create equity objects
aapl = Equity("AAPL", 150.00)
msft = Equity("MSFT", 200.00)

# get option chains for equities
aapl_options = get_option_chain(aapl)
msft_options = get_option_chain(msft)

# create option objects
aapl_call = Option(155.00, datetime(2022, 1, 1), "call", aapl)
aapl_put = Option(145.00, datetime(2022, 1, 1), "put", aapl)
msft_call = Option(205.00, datetime(2022, 1, 1), "call", msft)
msft_put = Option(195.00, datetime(2022, 1, 1), "put", msft)

# create portfolio object
portfolio = Portfolio([aapl_call, aapl_put, msft_call, msft_put], [aapl, msft])

# execute trades
buy_aapl_call = Trade(aapl_call, aapl, 10, 15.00)
execute_trade(buy_aapl_call, portfolio)

sell_msft_put = Trade(msft_put, msft, 5, 10.00)
execute_trade(sell_msft_put, portfolio)

# calculate portfolio value
portfolio_value = calculate_portfolio_value(portfolio)

# store portfolio value in database
db = Database()
db.store_portfolio_value(portfolio_value)

# improve recommendation system
improve_recommendations()

# run frontend
app.run()
