from flask import Blueprint, request, jsonify

bp = Blueprint('auctions', __name__, url_prefix='/api/auctions')

@bp.route('/', methods=['GET'])
def get_auctions():
    return jsonify({"message": "List of auctions"})

@bp.route('/', methods=['POST'])
def create_auction():
    return jsonify({"message": "Auction created"}), 201

@bp.route('/<auction_id>', methods=['GET'])
def get_auction(auction_id):
    return jsonify({"id": auction_id})