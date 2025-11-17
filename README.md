<h1 align="center">🐯 Mizzou Stock Data Visualizer</h1>
<p align="center"> A fully containerized Flask web application for visualizing stock market data using the Alpha Vantage API.<br> Styled using official <strong>Mizzou brand colors</strong> and deployed with Docker. </p>
<h2>📌 <u>Project Overview</u></h2>

The Mizzou Stock Data Visualizer is a web-based application that allows users to:

Select a stock symbol from a dynamically loaded S&P 500 dropdown.

Choose chart types (Line or Bar).

Choose time series options (Daily, Weekly, Monthly).

Select start and end dates for analysis.

Automatically fetch stock data from the Alpha Vantage API.

Display clean interactive charts generated with Plotly.

Run the entire application inside a Docker container for portability and consistency.

This project was built for Project 3A as part of the course requirement to convert a Python CLI tool into a fully interactive web app using Flask and Docker.

<h2>🏗️ <u>Technologies Used</u></h2>

Python 3.11

Flask

Plotly

Pandas

Requests

Docker & Docker Compose

HTML / CSS

Alpha Vantage API

Mizzou Color Branding

<h2>🎨 <u>Mizzou Theme Implementation</u></h2>

The application uses official University of Missouri (Mizzou) brand colors:

Primary Colors

Tiger Paw Black — #000000

Mizzou Gold — #FDB719

Neutral Colors

Black Tints 1–3 (Gray scale)

Accent Colors

Gold Tint 1–3

Alert colors for errors and warnings

Branding is applied through a custom mizzou.css file placed in /app/static/.

This ensures the application looks professionally themed, consistent, and compliant with Mizzou brand guidelines.

<h2>📂 <u>Project Structure</u></h2>
Project3a/
│
├── app/
│   ├── static/
│   │   └── mizzou.css
│   ├── templates/
│   │   └── stocks_home.html
│   ├── data/
│   │   └── stocks.csv
│   ├── utils/
│   │   └── load_symbols.py
│   ├── __init__.py
│   └── routes_stocks.py
│
├── stock_visualizer/
│   └── visualizer.py
│
├── .env                # Contains ALPHA_VANTAGE_API_KEY (not tracked in Git)
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.py
└── README.md

<h2>⚙️ <u>Installation & Setup</u></h2>
<h3>1️⃣ Clone the Repository</h3>
git clone https://github.com/AlexanderCoker/StockDataVisualizer.git
cd StockDataVisualizer

<h3>2️⃣ Create a Local <code>.env</code> File</h3>

Create .env in the project root:

ALPHA_VANTAGE_API_KEY=your_api_key_here


This file is ignored by Git and securely passed into Docker.

<h3>3️⃣ Build & Run with Docker</h3>
docker compose up --build


Then open:

http://localhost:5000

<h2>🧪 <u>Form Features & Validation</u></h2>

The application includes:

✔ Dynamic S&P 500 symbol dropdown

Loaded from stocks.csv using load_symbols.py.

✔ Input Validation

Invalid symbol

Invalid chart type

Invalid time series

Empty date fields

End date before start date

✔ Interactive Plotly Chart

Rendered directly below the form.

<h2>🐋 <u>Docker Configuration</u></h2>
Dockerfile

A lightweight Python 3.11-slim image that:

Installs dependencies

Copies project files

Exposes port 5000

Runs Flask via Gunicorn in production mode

docker-compose.yml

Loads environment variables from .env

Maps port 5000:5000

Builds the container

<h2>📜 <u>Usage</u></h2>

Select a stock symbol

Choose chart type

Choose time series

Select start & end dates

Click Generate Chart

View the interactive chart immediately below the form

<h2>🤝 <u>Credits</u></h2>

Developer: Alexander Coker
Project: Project 3A – Mizzou Stock Data Visualizer
Course: IT 4320 – Advanced Application Development

<h3>⚠️ Note</h3>

<em>This README was generated with the assistance of ChatGPT.</em>
