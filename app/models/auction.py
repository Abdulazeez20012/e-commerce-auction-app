from datetime import datetime


class Auction:
    STATUS = ['pending','active','closed','complete']

    def __init__(self, title, description, start_price, end_date, owner_id):
        self.title = title
        self.description = description
        self.start_price = float(start_price)
        self.current_price = float(start_price)
        self.end_date = end_date
        self.owner_id = owner_id
        self.status = 'pending'
        self.created_at = datetime.utcnow