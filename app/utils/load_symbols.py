import csv
import os

def load_symbols():
    # Directory where THIS file is located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Move UP one directory (from utils → app)
    app_dir = os.path.dirname(base_dir)

    # Path to the data folder inside project
    csv_path = os.path.join(app_dir, "data", "stocks.csv")

    symbols = []

    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            symbols.append(row["Symbol"])

    return symbols
