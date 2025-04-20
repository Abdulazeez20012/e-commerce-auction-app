from flask_socketio import SocketIO, emit

socketio = SocketIO(cors_allowed_origins="*")

def init_socketio(app):
    socketio.init_app(app)
    register_events()

def register_events():
    @socketio.on('connect')
    def handle_connect():
        print('Client connected')

    @socketio.on('disconnect')
    def handle_disconnect():
        print('Client disconnected')

    @socketio.on('join_auction')
    def handle_join_auction(auction_id):
        print(f'Client joined auction room: {auction_id}')

def broadcast_bid(auction_id, bid_data):
    socketio.emit('new_bid', bid_data, room=str(auction_id))