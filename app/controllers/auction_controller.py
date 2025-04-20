from flask import request, jsonify
from app.services import auction_service

def create_auction():
    data = request.json
    auction = auction_service.create_auction(
        data['title'],
        data['description'],
        float(data['start_price']),
        data['end_time'],
        int(data['seller_id'])
    )
    return jsonify(auction), 201

def get_auctions():
    auctions = auction_service.get_all_auctions()
    return jsonify(auctions), 200

def get_auction(auction_id):
    auction = auction_service.get_auction_by_id(auction_id)
    return jsonify(auction), 200