''''
The application should:

Ask the user to enter the stock symbol for the company they want data for.
Ask the user for the chart type they would like.
Ask the user for the time series function they want the api to use.
Ask the user for the beginning date in YYYY-MM-DD format.
Ask the user for the end date in YYYY-MM-DD format.
  The end date should not be before the begin date
Generate a graph and open in the user’s default browser.

    API KEY: 65QV08Y3LX4VJL5D

pip install plotly //graphing mod
pip install pandas
pip install requests
'''

from datetime import datetime
from input_handler import get_stock_symbol, get_chart_type, get_time_series
from visualizer import fetch_stock_data, plot_stock_chart

API_KEY = "65QV08Y3LX4VJL5D"

def validate_date(date_str):
    """Validate date format and ensure it's within supported range."""
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        if not (2005 <= date.year <= 2025):
            print("No data available for that year (must be between 2005–2025).")
            return None
        return date
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None


def calculate_duration(start, end, mode):
    """Return a duration string depending on the selected time series."""
    delta_days = abs((end - start).days)

    if mode == "2":  # Day
        return f"{delta_days} days"
    elif mode == "3":  # Week
        return f"{delta_days / 7:.2f} weeks"
    else:  # Month
        months = (end.year - start.year) * 12 + (end.month - start.month)
        return f"{abs(months)} months"


def build_alphavantage_url(symbol, time_series, interval=None, api_key=API_KEY):
    """Construct the Alpha Vantage API request URL."""
    base_url = "https://www.alphavantage.co/query?"
    function_map = {
        "1": "TIME_SERIES_INTRADAY",
        "2": "TIME_SERIES_DAILY",
        "3": "TIME_SERIES_WEEKLY",
        "4": "TIME_SERIES_MONTHLY"
    }

    function_name = function_map.get(time_series, "TIME_SERIES_DAILY")

    params = {
        "function": function_name,
        "symbol": symbol,
        "apikey": api_key
    }

    if function_name in ["TIME_SERIES_DAILY", "TIME_SERIES_WEEKLY", "TIME_SERIES_MONTHLY"]:
        params["outputsize"] = "full"
    if function_name == "TIME_SERIES_INTRADAY" and interval:
        params["interval"] = interval

    query_string = "&".join(f"{key}={value}" for key, value in params.items())
    return base_url + query_string


def get_date_input(prompt):
    """Prompt until a valid date is entered."""
    while True:
        user_input = input(prompt)
        date = validate_date(user_input)
        if date:
            return date


def get_user_input_and_build_url():
    """Handle user interaction and visualization workflow."""
    stock_symbol = get_stock_symbol()
    chart_type = get_chart_type()
    time_series = get_time_series()

    interval = "60min" if time_series == "1" else None

    # Fetch date range
    if time_series == "1":
        start_date = get_date_input("Enter the date (YYYY-MM-DD): ")
        end_date = None
    else:
        start_date = get_date_input("Enter the start date (YYYY-MM-DD): ")
        end_date = get_date_input("Enter the end date (YYYY-MM-DD): ")

        while end_date < start_date:
            print("End date cannot be before start date.")
            end_date = get_date_input("Enter the end date (YYYY-MM-DD): ")

        print("Duration:", calculate_duration(start_date, end_date, time_series))

    url = build_alphavantage_url(stock_symbol, time_series, interval)
    print(f"\nGenerated API URL:\n{url}\n")

    # Fetch and visualize
    data = fetch_stock_data(url)
    plot_stock_chart(data, chart_type, stock_symbol)


def main():
    """Main control loop."""
    while True:
        get_user_input_and_build_url()
        again = input("Would you like to view more stock data? (y/n): ").strip().lower()
        if again != "y":
            print("Buh-bye!")
            break


if __name__ == "__main__":
    main()
