import pytest
from flask_jwt_extended import create_access_token
from app import create_app
from app.services.database import mongo
from app.models.user import User

@pytest.fixture
def app():
    app, _ = create_app()
    app.config['TESTING'] = True
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/auction_app_test'
    with app.app_context():
        mongo.db.users.delete_many({})
        mongo.db.auctions.delete_many({})
        User.create('azeez', 'azeezmuhammad24434.com', 'mangowankillme')
        yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_token(app):
    with app.app_context():
        access_token = create_access_token(identity='azeez')
        return access_token

def test_create_auction(client, auth_token):
    response = client.post('/auctions',
        json={
            'title': 'ball',
            'description': 'panke',
            'start_price': 1000,
            'end_time': '2025-12-31T23:59:59'
        },
        headers={
            'Authorization': f'Bearer {auth_token}'
        }
    )
    assert response.status_code == 201
    assert 'auction_id' in response.json
    #
    # def test_create_auction_no_auth(client):
    #     # Test without authentication
    #     response = client.post('/auctions', json={...})
    #     assert response.status_code == 401
    #
    # def test_create_auction_invalid_data(client, auth_token):
    #     # Test with invalid data
    #     response = client.post('/auctions',
    #                            json={'title': ''},
    #                            headers={'Authorization': f'Bearer {auth_token}'}
    #                            )
    #     assert response.status_code == 400