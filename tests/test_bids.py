import pytest
from datetime import datetime, timedelta, timezone
from app import create_app
from app.services.database import mongo
from app.models.user import User
from app.models.auction import Auction
from app.models.bid import Bid
from flask_jwt_extended import create_access_token


@pytest.fixture
def app():
    app, _ = create_app()
    app.config['TESTING'] = True
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/auction_app_test'

    with app.app_context():
        mongo.db.users.delete_many({})
        mongo.db.auctions.delete_many({})
        mongo.db.bids.delete_many({})

        User.create('bidder1', 'bidder1@test.com', 'testpass')
        User.create('bidder2', 'bidder2@test.com', 'testpass')

        end_time = datetime.now(timezone.utc) + timedelta(days=1)
        Auction.create(
            title='Test Auction',
            description='Test Item',
            start_price=100.0,
            end_time=end_time,
            creator_id='user123'
        )

        yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def auth_tokens(app):
    with app.app_context():
        return {
            'bidder1': create_access_token(identity='bidder1'),
            'bidder2': create_access_token(identity='bidder2')
        }


def test_place_valid_bid(client, auth_tokens):
    auction = Auction.find_all_active()[0]

    bid_amount = round(auction['start_price'] * 1.1, 2)

    response = client.post(
        f'/auctions/{auction["_id"]}/bids',
        json={'amount': bid_amount},
        headers={'Authorization': f'Bearer {auth_tokens["bidder1"]}'}
    )

    print(f"Response: {response.status_code}, {response.json}")

    assert response.status_code == 201
    assert 'bid_id' in response.json

    bids = Bid.find_by_auction(auction["_id"])
    assert len(bids) == 1
    assert bids[0]['amount'] == bid_amount