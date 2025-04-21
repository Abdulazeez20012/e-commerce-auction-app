from datetime import datetime, timezone
from app.services.database import mongo

class Bid:
    @staticmethod
    def create(auction_id, user_id, amount):
        return mongo.db.bids.insert_one({
            'auction_id': auction_id,
            'user_id': user_id,
            'amount': float(amount),
            'created_at': datetime.now(timezone.utc),
        })

    @staticmethod
    def find_by_auction(auction_id):
        return list(mongo.db.bids.find({'auction_id': auction_id}).sort('created_at', -1))

    @staticmethod
    def get_highest_bid(auction_id):
        return mongo.db.bids.find_one(
            {'auction_id': auction_id},
            sort=[('amount', -1)]
        )