from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.auction_service import AuctionService
from datetime import datetime


class AuctionController:
    @staticmethod
    @jwt_required()
    def create_auction():
        try:
            data = request.get_json()
            creator_id = get_jwt_identity()

            required_fields = ['title', 'description', 'start_price', 'end_time']
            if not all(field in data for field in required_fields):
                return jsonify({'error': 'Missing required fields'}), 400

            if float(data['start_price']) <= 0:
                return jsonify({'error': 'Start price must be positive'}), 400

            end_time = datetime.fromisoformat(data['end_time'])
            if end_time <= datetime.now():
                return jsonify({'error': 'End time must be in the future'}), 400

            auction_id = AuctionService.create_auction(
                title=data['title'],
                description=data['description'],
                start_price=data['start_price'],
                end_time=end_time,
                creator_id=creator_id
            )

            return jsonify({'auction_id': auction_id}), 201

        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': 'Server error'}), 500

    @staticmethod
    def get_auctions():
        try:
            auctions = AuctionService.get_active_auctions()
            return jsonify(auctions), 200
        except Exception as e:
            return jsonify({'error': 'Server error'}), 500

    @staticmethod
    @jwt_required()
    def get_auction(auction_id):
        try:
            auction, error = AuctionService.get_auction_details(auction_id)
            if error:
                return jsonify({'error': error}), 404
            return jsonify(auction), 200
        except Exception as e:
            return jsonify({'error': 'Server error'}), 500

    @staticmethod
    @jwt_required()
    def place_bid(auction_id):
        try:
            data = request.get_json()
            user_id = get_jwt_identity()

            if 'amount' not in data:
                return jsonify({'error': 'Bid amount is required'}), 400

            bid_id, error = AuctionService.place_bid(
                auction_id=auction_id,
                user_id=user_id,
                amount=data['amount']
            )

            if error:
                return jsonify({'error': error}), 400

            return jsonify({'bid_id': bid_id}), 201

        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': 'Server error'}), 500