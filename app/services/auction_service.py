from datetime import datetime

from app.services.database import MongoDBService


class AuctionService:
    def __init__(self):
        self.db = MongoDBService()
        self.auctions = self.db.get_collection('auctions')
        self.bids = self.db.get_collection('bids')

    def create_auction(self, auction_data):
        result = self.auctions.insert_one(auction_data)
        return str(result.inserted_id)

    def get_auction(self, auction_id):
        return self.auctions.fine_one({'_id': auction_id})

    def place_bid(self, auction_id, user_id, amount):
        auction = self.get_auction(auction_id)
        if not auction or auction['status'] != 'active':
            return False
        if amount <= auction['current_price']:
            return False

        bid_data = {
            'auction_id' : auction_id,
            'user_id' : user_id,
            'amount' : amount,
            'created_at' : datetime.utcnow()
        }
        self.bids.insert_one(bid_data)
        self.auctions.update.update_one(
            {'_id': auction_id},
            {'$set': {'current_price': amount}}
        )
        return True