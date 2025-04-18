from app.services.auth_service import AuthService


class AuthController:
    def __init__(self):
        self.auth_service = AuthService()