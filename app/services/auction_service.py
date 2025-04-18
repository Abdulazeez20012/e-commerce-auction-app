from app.services.database import MongoDBService


class AuctionService:
    def __init__(self):
        self.db = MongoDBService()
        self.auctions = self.db.get_collection('auctions')
        self.bids = self.db.get_collection('bids')

    def create_auction(self, auction_data):
        result = self.auctions.insert_one(auction_data)
        return str(result.inserted_id)