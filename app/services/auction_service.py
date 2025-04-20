from ..models.auction import Auction
from ..models.bid import Bid
from ..services.database import mongo
from bson import ObjectId


def create_auction(title, description, start_price, end_time, seller_id):
    auction = Auction(title, description, start_price, end_time, seller_id)
    result = mongo.db.auctions.insert_one(auction.to_dict())
    return {'id': str(result.inserted_id), 'title': title, 'current_price': start_price}


def get_all_auctions():
    return list(mongo.db.auctions.find())


def get_auction_by_id(auction_id):
    return mongo.db.auctions.find_one({'_id': ObjectId(auction_id)})


def place_bid(auction_id, user_id, amount):
    auction = mongo.db.auctions.find_one({'_id': ObjectId(auction_id)})
    if not auction:
        return {'error': 'Auction not found'}, 404

    if amount <= auction['current_price']:
        return {'error': 'Bid must be higher than current price'}, 400

    bid = Bid(amount, user_id, auction_id)
    mongo.db.bids.insert_one(bid.to_dict())

    # Update auction current price
    mongo.db.auctions.update_one(
        {'_id': ObjectId(auction_id)},
        {'$set': {'current_price': amount}}
    )

    return {'message': 'Bid placed successfully'}, 201


def get_bids_for_auction(auction_id):
    return list(mongo.db.bids.find({'auction_id': auction_id}).sort('amount', -1))