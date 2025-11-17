🐯 Mizzou Stock Data Visualizer (Project 3A)

A fully-Dockerized, Flask-powered web application that visualizes stock price data using the Alpha Vantage API.
This project converts the console-based stock visualizer from Project 3 into a full web interface with dropdown symbol selection, chart rendering, and complete input validation — all wrapped in a Mizzou-themed UI following official brand guidelines.

This project fulfills all requirements for IT 4320 – Project 3A.

🚀 Features
✔ Fully-functional Flask Web App

Web interface replaces console input

GET/POST routes for clean data handling

Mizzou-themed page layout and colors

Stock charts generated directly in-browser

✔ Dynamic S&P 500 Stock Symbol Dropdown

Loads symbols from stocks.csv (not hard-coded)

Automatically populates on page load

✔ Alpha Vantage API Integration

Fetches time series data (Daily / Weekly / Monthly)

Displays stock trend using Plotly

✔ Full Input Validation (per rubric)

Valid symbol check

Valid chart type

Valid time series selection

Start/end date validation

End date > start date enforcement

User feedback displayed directly on page

✔ Plotly Chart Rendering

Line or bar chart options

Displays directly below form

Styled to match the Mizzou theme

✔ Dockerized Deployment

Created Dockerfile for building the image

Docker Compose used to run the app

API key securely loaded via .env (not in image)

Ready to run on any machine with Docker installed

🗂 Project Structure
Project3a/
│
├── app/
│   ├── templates/
│   │   └── stocks_home.html
│   ├── utils/
│   │   └── load_symbols.py
│   ├── routes_stocks.py
│   └── __init__.py
│
├── stock_visualizer/
│   └── visualizer.py
│
├── data/
│   └── stocks.csv
│
├── run.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

🧪 Requirements

Installations inside Docker:

Flask
pandas
plotly
requests
gunicorn


The requirements.txt file installs everything automatically.

🔑 Environment Variables

The application requires an Alpha Vantage API key.

Create a .env file in the project root:

ALPHA_VANTAGE_API_KEY=YOUR_KEY_HERE


⚠️ .env is ignored in .gitignore to protect sensitive information.

🐳 Running the Project with Docker
1. Build & Run the Application
docker compose up --build

2. Access the Web App

Open your browser to:

http://localhost:5000

🖼 Web Interface

The web form provides:

Stock Symbol Dropdown (loaded from S&P 500 CSV)

Chart Type (Line / Bar)

Time Series (Daily / Weekly / Monthly)

Start Date / End Date (with error validation)

Chart output renders immediately below the form.

🎨 Mizzou-Themed UI

This project follows MU Brand Guidelines:

Primary Colors

Tiger Paw Black – #000000

Mizzou Gold – #FDB719

Neutral Colors

Black Tint 1 – #333333

Black Tint 2 – #989898

Black Tint 3 – #D4D4D4

Design targets:

≥70% primary colors

≤25% neutrals

≤5% accents

The form, background, labels, headings, and chart areas incorporate these color requirements.
