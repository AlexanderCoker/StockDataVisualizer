<h1 align="center">🐯 Mizzou Stock Data Visualizer</h1>
<p align="center">
A fully containerized Flask web application for visualizing stock market data using the Alpha Vantage API.<br>
Styled using official <strong>Mizzou brand colors</strong> and deployed with Docker.
</p>

---

## 📌 Project Overview

The **Mizzou Stock Data Visualizer** is a Flask-based web application that allows users to:

- Select a stock symbol from a dynamically loaded **S&P 500 dropdown**
- Choose chart types (**Line** or **Bar**)
- Choose time series (**Daily**, **Weekly**, **Monthly**)
- Select **start and end dates**
- Automatically fetch stock data using the **Alpha Vantage API**
- View clean, interactive charts built with **Plotly**
- Run the entire application inside **Docker** for portability and consistency

This project was created for **Project 3A**, converting a Python CLI stock tool into a fully interactive Flask web app.

---

## 🏗️ Technologies Used

- Python 3.11  
- Flask  
- Plotly  
- Pandas  
- Requests  
- Docker & Docker Compose  
- HTML / CSS  
- Alpha Vantage API  
- Mizzou Color Branding  

---

## 🎨 Mizzou Theme Implementation

The application uses the official **University of Missouri brand colors**.

### **Primary Colors**
- **Tiger Paw Black** — `#000000`  
- **Mizzou Gold** — `#FDB719`

### **Neutral Colors**
- Black Tints 1–3 (grayscale)

### **Accent Colors**
- Gold Tint 1–3  
- Alert colors for form errors & warnings  

Branding is implemented in a custom stylesheet:

```
/app/static/mizzou.css
```

This ensures the UI remains clean, professional, and compliant with Mizzou branding guidelines.

---

## 📂 Project Structure

```
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
├── .env                # Alpha Vantage API key (not committed)
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.py
└── README.md
```

---

## ⚙️ Installation & Setup

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/AlexanderCoker/StockDataVisualizer.git
cd StockDataVisualizer
```

---

### **2️⃣ Create a Local `.env` File**

Add the following to a new `.env` file in the project root:

```env
ALPHA_VANTAGE_API_KEY=your_api_key_here
```

This file is ignored by Git and passed securely into Docker.

---

### **3️⃣ Build & Run with Docker**

```bash
docker compose up --build
```

Then open your browser to:

```
http://localhost:5000
```

---

## 🧪 Form Features & Validation

The application includes:

### ✔ Dynamic S&P 500 Symbol Dropdown
Loaded from `stocks.csv` via `load_symbols.py`.

### ✔ Input Validation
- Invalid symbol  
- Invalid chart type  
- Invalid time series  
- Empty date fields  
- End date before start date  

### ✔ Interactive Plotly Chart
Displayed directly below the form after submission.

---

## 🐋 Docker Configuration

### **Dockerfile**
A lightweight `python:3.11-slim` image that:

- Installs dependencies  
- Copies project files  
- Exposes port 5000  
- Runs Flask via **Gunicorn** in production mode  

### **docker-compose.yml**
- Loads `.env` environment variables  
- Maps port **5000:5000**  
- Builds and runs the container  

---

## 📜 Usage

1. Select a stock symbol  
2. Choose chart type  
3. Choose time series  
4. Select start & end dates  
5. Click **Generate Chart**  
6. View the interactive Plotly chart  

---

## 🤝 Credits

**Developer:** Alexander Coker  
**Project:** Project 3A – Mizzou Stock Data Visualizer  
**Course:** IT 4320 – Advanced Application Development  

---

### ⚠️ Note
*This README was generated with assistance from ChatGPT.*
