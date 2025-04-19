from flask import Blueprint

from app.controllers.auth_controller import AuthController
from app.controllers.bid_controller import BidController


def register_routes(app):
    api = Blueprint('api',__name__, url_prefix='/api')

    auth_controller = AuthController()
    auction_controller = AuthController()
    bid_controller = BidController()

    api.add_url_rule('register', view_func=auth_controller.register, methods=['POST'])
    api.add_url_rule('/login', view_func=auction_controller.login, methods=['POST'])
    