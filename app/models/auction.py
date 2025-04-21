from datetime import datetime, timezone
from app.services.database import mongo

class Auction:
    @staticmethod
    def create(title, description, start_price, end_time, creator_id, status='active'):
        return mongo.db.auctions.insert_one({
            'title': title,
            'description': description,
            'start_price': float(start_price),
            'current_price': float(start_price),
            'end_time': end_time,
            'creator_id': creator_id,
            'status': status,
            'created_at': datetime.now(timezone.utc),
            'updated_at': datetime.now(timezone.utc)
        })

    @staticmethod
    def find_all_active():
        now = datetime.utcnow()
        return list(mongo.db.auctions.find({
            'end_time': {'$gt': now},
            'status': 'active'
        }).sort('created_at', -1))

    @staticmethod
    def find_by_id(auction_id):
        return mongo.db.auctions.find_one({'_id': auction_id})

    @staticmethod
    def update_price(auction_id, new_price):
        return mongo.db.auctions.update_one(
            {'_id': auction_id},
            {'$set': {
                'current_price': new_price,
                'updated_at': datetime.utcnow()
            }}
        )

    @staticmethod
    def close_auction(auction_id):
        return mongo.db.auctions.update_one(
            {'_id': auction_id},
            {'$set': {
                'status': 'closed',
                'updated_at': datetime.utcnow()
            }}
        )