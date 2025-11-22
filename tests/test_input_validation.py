import pytest
from datetime import datetime
from stock_visualizer.input_validation import (
    validate_symbol,
    validate_chart_type,
    validate_time_series,
    validate_date,
)

def test_valid_symbol():
    assert validate_symbol("AAPL") == "AAPL"

def test_invalid_symbol_lower():
    with pytest.raises(ValueError):
        validate_symbol("aapl")

def test_invalid_symbol_length():
    with pytest.raises(ValueError):
        validate_symbol("ABCDEFGH")

def test_valid_chart_type():
    assert validate_chart_type("1") == "1"
    assert validate_chart_type("2") == "2"

def test_invalid_chart_type():
    with pytest.raises(ValueError):
        validate_chart_type("3")

def test_valid_time_series():
    for ts in ["1", "2", "3", "4"]:
        assert validate_time_series(ts) == ts

def test_invalid_time_series():
    with pytest.raises(ValueError):
        validate_time_series("5")

def test_valid_date():
    assert validate_date("2023-12-31") == datetime(2023, 12, 31)

def test_invalid_date_format():
    with pytest.raises(ValueError):
        validate_date("31-12-2023")

def test_invalid_date_logic():
    with pytest.raises(ValueError):
        validate_date("2023-02-30")
