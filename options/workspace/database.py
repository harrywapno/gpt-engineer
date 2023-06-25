import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('portfolio.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS portfolio_value
                                (date text, value real)''')

    def store_portfolio_value(self, value: float):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO portfolio_value VALUES (?, ?)", (date, value))
        self.conn.commit()

    def get_portfolio_value(self) -> float:
        self.cursor.execute("SELECT value FROM portfolio_value ORDER BY date DESC LIMIT 1")
        value = self.cursor.fetchone()[0]
        return value
