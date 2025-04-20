from flask import Blueprint, request, jsonify

bp = Blueprint('auth_api', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    return jsonify({"message": "User registered"}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return jsonify({"token": "sample-token"}), 200