# visualizer.py - Generate HTML Plotly charts for Flask

import requests
import plotly.express as px
import pandas as pd

def fetch_stock_data(url):
    """Fetch stock data from Alpha Vantage."""
    try:
        response = requests.get(url)
        data = response.json()

        time_series_keys = [
            "Time Series (60min)",
            "Time Series (Daily)",
            "Weekly Time Series",
            "Monthly Time Series"
        ]

        for key in time_series_keys:
            if key in data:
                return data[key]

        print("Error: Time series data was not found in the response.")
        return None

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None


def generate_stock_chart_html(time_series_data, chart_type="Line", symbol="N/A"):
    """Return an HTML string containing the interactive Plotly chart."""
    if not time_series_data:
        return "<p>No data available to plot.</p>"

    # Convert to DataFrame
    df = pd.DataFrame.from_dict(time_series_data, orient='index')
    df = df.sort_index()
    df["date"] = df.index
    df["close"] = df["4. close"].astype(float)

    # Only last 20 for readability
    df = df.tail(20)

    if chart_type == "Bar":
        fig = px.bar(df, x="date", y="close",
                     title=f"{symbol} - Last 20 Closing Prices")
    else:
        fig = px.line(df, x="date", y="close",
                      title=f"{symbol} - Last 20 Closing Prices")

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Closing Price",
        xaxis_tickangle=-45
    )

    # Return HTML code instead of fig.show()
    return fig.to_html(full_html=False)
