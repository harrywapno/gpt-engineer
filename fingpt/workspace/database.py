import sqlite3
from stock import Stock, Option

class Database:
    def __init__(self, db_name='options.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS stocks
                          (symbol text PRIMARY KEY)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS options
                          (id integer PRIMARY KEY, stock_symbol text, last real, ask real, bid real, volume integer, implied_volatility real)''')
        self.conn.commit()

    def save_stock_data(self, stock: Stock):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO stocks (symbol) VALUES (?)", (stock.symbol,))
        self.conn.commit()

    def save_option_data(self, option: Option):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO options (stock_symbol, last, ask, bid, volume, implied_volatility) VALUES (?, ?, ?, ?, ?, ?)", (option.stock_symbol, option.last, option.ask, option.bid, option.volume, option.implied_volatility))
        self.conn.commit()
