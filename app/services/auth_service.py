from werkzeug.security import check_password_hash

from ..models.user import User
from ..services.database import mongo


def register_user(username, email, password):
    if mongo.db.users.find_one({'email': email}):
        return {'error': 'Email already exists'}, 400

    user = User(username, email, password)
    mongo.db.users.insert_one(user.to_dict())
    return {'message': 'User created successfully'}, 201


def login_user(email, password):
    user = mongo.db.users.find_one({'email': email})
    if not user or not check_password_hash(user['password_hash'], password):
        return {'error': 'Invalid credentials'}, 401

    return f"user-{str(user['_id'])}-token"