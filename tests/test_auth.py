import pytest
from app import create_app
from app.services.database import mongo
from app.models.user import User


@pytest.fixture
def app():
    app, _ = create_app()
    app.config['TESTING'] = True
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/auction_app_test'
    app.config['WTF_CSRF_ENABLED'] = False

    with app.app_context():
        mongo.db.users.delete_many({})
        yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_register(client):
    response = client.post('/auth/register', json={
        'username': 'azeez',
        'email': 'azeezmuhammad24434.com',
        'password': 'mangowankillme'
    })

    assert response.status_code == 201
    assert 'user_id' in response.json

    with client.application.app_context():
        user = User.find_by_username('azeez')
        assert user is not None
        assert user['email'] == 'azeezmuhammad24434.com'