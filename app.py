from app import create_app
from config import Config

app, socketio = create_app()

if __name__ == '__main__':
    socketio.run(app, debug=Config.DEBUG)