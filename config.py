import os


class Config:
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/auction_app'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Mangodb wan kill me'