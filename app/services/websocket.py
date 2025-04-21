from datetime import datetime

from flask_socketio import SocketIO, emit
from app.services.database import mongo

from app.models.auction import Auction
from app.models.bid import Bid

socketio = SocketIO()


def init_websocket(app):
    socketio.init_app(app, cors_allowed_origins="*")


@socketio.on('join_auction')
def handle_join_auction(data):
    auction_id = data['auction_id']
    emit('auction_update', {'message': f'Joined auction {auction_id}'}, room=auction_id)


@socketio.on('place_bid')
def handle_place_bid(data):
    auction_id = data['auction_id']
    user_id = data['user_id']
    amount = data['amount']

    bid_id = Bid.create(auction_id, user_id, amount)
    Auction.update_price(auction_id, amount)

    bid = {
        'id': str(bid_id.inserted_id),
        'user_id': user_id,
        'amount': amount,
        'timestamp': datetime.utcnow().isoformat()
    }

    emit('new_bid', bid, room=auction_id)