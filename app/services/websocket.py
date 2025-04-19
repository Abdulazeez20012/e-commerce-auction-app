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
