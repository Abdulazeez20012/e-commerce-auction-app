from flask import request, jsonify
from app.services.auth_service import AuthService


class AuthController:
    @staticmethod
    def register():
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        user_id, error = AuthService.register_user(username, email, password)
        if error:
            return jsonify({'error': error}), 400

        return jsonify({'user_id': user_id}), 201

    @staticmethod
    def login():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        result, error = AuthService.login_user(username, password)
        if error:
            return jsonify({'error': error}), 401

        return jsonify(result), 200