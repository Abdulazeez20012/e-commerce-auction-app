def register_routes(app):
    from app.controllers import auth_controller
    app.register_blueprint(auth_controller.bp)
