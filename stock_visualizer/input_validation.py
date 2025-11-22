import re
from datetime import datetime


def validate_symbol(symbol: str) -> str:
    """
    Symbol must be 1–7 alphabetic characters, all uppercase.
    """
    if not isinstance(symbol, str):
        raise ValueError("Symbol must be a string.")

    if not re.fullmatch(r"[A-Z]{1,7}", symbol):
        raise ValueError("Symbol must be 1–7 uppercase letters (A–Z).")

    return symbol


def validate_chart_type(chart_type: str) -> str:
    """
    Chart type must be '1' or '2'.
    """
    if chart_type not in ("1", "2"):
        raise ValueError("Chart type must be '1' or '2'.")
    return chart_type


def validate_time_series(time_series: str) -> str:
    """
    Time series must be '1', '2', '3', or '4'.
    """
    if time_series not in ("1", "2", "3", "4"):
        raise ValueError("Time series must be 1–4.")
    return time_series


def validate_date(date_str: str) -> datetime:
    """
    Date must be in format YYYY-MM-DD and must be a valid calendar date.
    """
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Date must be in format YYYY-MM-DD and valid.")


# Optional (for clarity)
def validate_start_date(date_str: str) -> datetime:
    return validate_date(date_str)


def validate_end_date(date_str: str) -> datetime:
    return validate_date(date_str)
