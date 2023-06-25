from flask import Flask, render_template
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/')
def index():
    portfolio_value = db.get_portfolio_value()
    return render_template('index.html', portfolio_value=portfolio_value)
