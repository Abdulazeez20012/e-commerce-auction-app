from flask import request, jsonify

from app.services.auth_service import AuthService


class AuthController:
    def __init__(self):
        self.auth_service = AuthService()
    def register(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not all([username, email, password]):
            return jsonify({'error':'missing required fields'}),400

        user_id = self.auth_service.register_user(username, email, password)
        if not user_id:
            return jsonify({'error': 'username or email already exists'}),400
        return jsonify({'message': 'user registered successfully', 'user_id': user_id}), 201

    def login(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not all([email, password]):
            return jsonify({'error': 'Missing email or password'}),400
