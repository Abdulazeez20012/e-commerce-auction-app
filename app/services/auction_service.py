from datetime import datetime

from app.models.auction import Auction
from app.models.bid import Bid


class AuctionService:
    @staticmethod
    def create_auction(title, description, start_price, end_time, creator_id):
        auction_id = Auction.create(title, description, start_price, end_time, creator_id)
        return str(auction_id.inserted_id)

    @staticmethod
    def get_active_auctions():
        return Auction.find_all_active()

    @staticmethod
    def get_auction_details(auction_id):
        auction = Auction.find_by_id(auction_id)
        if not auction:
            return None, 'Auction not found'

        bids = Bid.find_by_auction(auction_id)
        return {'auction': auction, 'bids': bids}, None

    @staticmethod
    def place_bid(auction_id, user_id, amount):
        auction = Auction.find_by_id(auction_id)
        if not auction or auction['status'] != 'active':
            return None, 'Auction not available for bidding'

        if amount <= auction['current_price']:
            return None, 'Bid amount must be higher than current price'

        bid_id = Bid.create(auction_id, user_id, amount)
        Auction.update_price(auction_id, amount)

        return str(bid_id.inserted_id), None