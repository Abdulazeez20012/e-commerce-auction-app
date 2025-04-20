from flask import Flask
from app.routes import register_routes


def create_app():
    app = Flask(__name__)

    try:
        app.config.from_pyfile('config.py')
    except FileNotFoundError:
        app.config['SECRET_KEY'] = 'Mangodb wan kill me '
        app.config['MONGO_URI'] = 'mongodb://localhost:27017/auction_db'

    register_routes(app)
    return app