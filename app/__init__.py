from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from app.services.database import mongo
from app.services.websocket import init_websocket, socketio
from app.routes import bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    init_websocket(app)
    JWTManager(app)

    app.register_blueprint(bp)

    return app, socketio