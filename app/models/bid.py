from datetime import datetime

class Bid:
    def __init__(self, auction_id, user_id, amount):
        self.auction_id = auction_id
        self.user_id = user_id
        self.amount = float(amount)
        self.created_at = datetime.utcnow()