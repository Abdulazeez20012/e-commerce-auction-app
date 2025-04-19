from datetime import datetime

from flask import request, jsonify

from app.services.auction_service import AuctionService


class AuctionController:
    def __init__(self):
        self.auction_service = AuctionService

    def create_auction(self, user_id):
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        start_price = data.get('start_price')
        end_date = data.get('end_date')

        if not all([title, start_price, end_date]):
            return jsonify({'error': 'Missing required feilds'}), 400

        try:
            end_date = datetime.fromisoformat(end_date)
            if end_date <= datetime.utcnow():
                return jsonify({'error':'End date must be in the future'}), 400
        except ValueError:
            return  jsonify({'error': 'Invalid date format'}), 400
        auction_id = self.auction_service.create_auction(
            title, description, start_price, end_date, user_id
        )
        return  jsonify({'message': 'Auction created', 'auction_id': auction_id}), 201

    def get_all_auctions(self):
        auctions = self.auction_service.get_auctions()
        for auction in auctions:
            auction['-id'] = str(auction['_id'])
            auction['owner-id'] = str(auction['owner_id'])
        return jsonify(auctions),200
    def get_auction(self, auction_id):
        auction = self.auction_service.get_auction_by_id(auction_id)
        if not auction:
            return jsonify({'error': 'Auction not found '}), 400

        auction['-id'] = str(auction['_id'])
        auction['owner-id'] = str(auction['owner_id'])
        return jsonify(auction), 200