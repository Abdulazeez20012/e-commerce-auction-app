from app.controllers import auction_bp, auth_bp


def register_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(auction_bp)
    # app.register_blueprint(bid_bp)

    @app.route('/')
    def home():
        return "Welcome to Auction App"