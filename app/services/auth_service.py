from flask_jwt_extended import create_access_token
from app.models.user import User


class AuthService:
    @staticmethod
    def register_user(username, email, password):
        if User.find_by_username(username):
            return None, 'Username already exists'
        user_id = User.create(username, email, password)
        return str(user_id.inserted_id), None

    @staticmethod
    def login_user(username, password):
        user = User.find_by_username(username)
        if not user or not User.verify_password(user, password):
            return None, 'Invalid credentials'

        access_token = create_access_token(identity=str(user['_id']))
        return {'access_token': access_token, 'user_id': str(user['_id'])}, None