from datetime import datetime


class Bid:
    def __init__(self, amount, user_id, auction_id):
        self.amount = amount
        self.user_id = user_id
        self.auction_id = auction_id
        self.time_placed = datetime.utcnow()

    def to_dict(self):
        return {
            'amount': self.amount,
            'user_id': self.user_id,
            'auction_id': self.auction_id,
            'time_placed': self.time_placed
        }