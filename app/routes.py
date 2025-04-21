from flask import Blueprint
# from app.controllers.auth_controller import AuthController
from app.controllers.auction_controller import AuctionController

bp = Blueprint('api', __name__)

bp.add_url_rule('/auctions', 'create_auction', AuctionController.create_auction, methods=['POST'])
bp.add_url_rule('/auctions', 'get_auctions', AuctionController.get_auctions, methods=['GET'])
bp.add_url_rule('/auctions/<auction_id>', 'get_auction', AuctionController.get_auction, methods=['GET'])
bp.add_url_rule('/auctions/<auction_id>/bids', 'place_bid', AuctionController.place_bid, methods=['POST'])