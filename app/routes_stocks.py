from flask import Blueprint, render_template, request
from stock_visualizer.visualizer import fetch_stock_data, generate_stock_chart_html
from app.utils.load_symbols import load_symbols
import os

from stock_visualizer.input_validation import (
    validate_symbol,
    validate_chart_type,
)


stocks_bp = Blueprint('stocks', __name__, template_folder='templates')

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"

if not API_KEY:
    raise ValueError("Missing ALPHA_VANTAGE_API_KEY environment variable.")

@stocks_bp.route('/stocks', methods=['GET', 'POST'])
def stocks_home():
    chart_html = None

    # Load symbols from CSV
    symbols = load_symbols()

    if request.method == 'POST':
          try:
            symbol = validate_symbol(request.form["symbol"].upper())
            chart_type = validate_chart_type(request.form["chart_type"])
    
            url = f"{BASE_URL}?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
            data = fetch_stock_data(url)
            chart_html = generate_stock_chart_html(data, chart_type, symbol)
    
        except ValueError as ve:
            chart_html = f"<p style='color:red;'>Input error: {ve}</p>"


    return render_template('stocks_home.html', chart_html=chart_html, symbols=symbols)

@stocks_bp.route('/', methods=['GET', 'POST'])
def home():
    return stocks_home()
