import os

from dotenv import load_dotenv
from flask_pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client.auction_db

db.auctions.insert_one({"title": "Test Auction","price": 100})
