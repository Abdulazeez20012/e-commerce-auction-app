from app.models.user import User
from app.services.database import MongoDBService

class AuthService:
    def __init__(self):
        self.db = MongoDBService()
        self.users = self.db.get_collection('users')

    def register_user(self, username, email, password):
        if self.users.find_one({'$or': [{'username': username}, {'email': email}]}):
            return None
        user = User(username, email, password)
        result = self.users.insert_one(user.__dict__)
        return str(result.inserted_id)

    def authenticate_user(self, email, password):
        user_data = self.users.find_one({'email': email})
        if not user_data:
            return None
        user = User(user_data['username'], user_data['email'], user_data['password'])
        return user if user.verify_password(password) else None

