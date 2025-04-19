from app.services.auction_service import AuctionService


class WebSocketService:
    def __init__(self, socketio):
        self.socketio = socketio
        self.auction_service = AuctionService
        self.register_handlers()

    def register_handlers(self):
        @self.socketio.on('connect')
        def handle_conect():
            print('Client connected')

        @self.socketio.on('disconnect')
        def handle_disconnect():
            print('Client disconnected')

        @self.socketio.on('join_auction')
        def handle_join_auction(auction_id):
            print(f'Client joined auction {auction_id}')

        @self.socketio.on('place_bid')
        def handle_place_bid(data):
            auction_id = data.get('auction_id')
            user_id = data.get('user_id')
            amount = data.get('amount')


            success = self.auction_service.place_bid(auction_id, user_id, amount)
            if success:
                auction = self.auction_service.get_auction_by_id(auction_id)
                self.socketio.emit('bid_update', {
                    'auction_id': str(auction_id),
                    'current_price': auction['current_price'],
                    'bidder_id': user_id
                }, room=auction_id)
                return {'success': True}
            return {'success': False, 'error': 'Bid not accepted'}




