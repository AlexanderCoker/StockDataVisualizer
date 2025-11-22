# stock_visualizer/input_validation.py
import re
from datetime import datetime

def validate_symbol(symbol: str) -> str:
    if not isinstance(symbol, str):
        raise ValueError("Symbol must be a string.")
    if not re.fullmatch(r"[A-Z]{1,7}", symbol):
        raise ValueError("Symbol must be 1–7 capital letters.")
    return symbol

def validate_chart_type(chart_type: str) -> str:
    if chart_type not in ("1", "2"):
        raise ValueError("Chart type must be '1' or '2'.")
    return chart_type

def validate_time_series(time_series: str) -> str:
    if time_series not in ("1", "2", "3", "4"):
        raise ValueError("Time series must be 1–4.")
    return time_series

def validate_date(date_str: str) -> datetime:
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Date must be YYYY-MM-DD.")
