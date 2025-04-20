from flask import request, jsonify
from app.services import auction_service, websocket


def place_bid(auction_id):
    data = request.json
    bid = auction_service.place_bid(
        int(auction_id),
        int(data['user_id']),
        float(data['amount'])
    )

    websocket.broadcast_bid(auction_id, {
        'user_id': bid['user_id'],
        'amount': bid['amount'],
        'auction_id': auction_id
    })

    return jsonify(bid), 201


def get_bids(auction_id):
    bids = auction_service.get_bids_for_auction(auction_id)
    return jsonify(bids), 200