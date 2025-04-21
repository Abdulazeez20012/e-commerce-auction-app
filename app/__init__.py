from flask import Flask
from flask_pymongo import PyMongo
from flask_socketio import SocketIO

mongo = PyMongo()
socketio = SocketIO()

def create_app():
    app = Flask(__name__, 
               template_folder='templates', 
               static_folder='static')
    
    app.config.from_object('config.Config')
    
    mongo.init_app(app)
    socketio.init_app(app)
    
    from app.routes import register_routes
    register_routes(app)
    
    return app