from flask import Flask
from app.routes_stocks import stocks_bp

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "your_secret_key"
    app.register_blueprint(stocks_bp)

    return app
