from datetime import datetime, timezone
from app.services.database import mongo
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    @staticmethod
    def create(username, email, password):
        hashed_password = generate_password_hash(password)
        return mongo.db.users.insert_one({
            'username': username,
            'email': email,
            'password': hashed_password,
            'created_at': datetime.now(timezone.utc),
            'updated_at': datetime.now(timezone.utc)
        })

    @staticmethod
    def find_by_username(username):
        return mongo.db.users.find_one({'username': username})

    @staticmethod
    def verify_password(user, password):
        return check_password_hash(user['password'], password)