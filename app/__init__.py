import socketio
from flask import Flask

from app.services.database import MongoDBService
from config import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    MongoDBService()

    register_routes(app)

    from app.services.websocket import WebSocketService
    socketio.init_app(app)
    WebSocketService(socketio)

    return app