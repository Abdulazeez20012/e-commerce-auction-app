from datetime import datetime

class Auction:
    def __init__(self, title, description, start_price, end_time, seller_id):
        self.title = title
        self.description = description
        self.start_price = start_price
        self.current_price = start_price
        self.start_time = datetime.utcnow()
        self.end_time = end_time
        self.seller_id = seller_id
        self.is_active = True

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'start_price': self.start_price,
            'current_price': self.current_price,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'seller_id': self.seller_id,
            'is_active': self.is_active
        }