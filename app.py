from flask import Flask
from config import Config
from app.services.database import mongo, init_db

app = Flask(__name__)
app.config.from_object(Config)

init_db(app)

from app.controllers.auth_controller import register

app.add_url_rule('/register', view_func=register, methods=['POST'])

from app.controllers import auth_controller, auction_controller, bid_controller

app.add_url_rule('/login', view_func=auth_controller.login, methods=['POST'])

if __name__ == '__main__':
    app.debug = True
    app.run()