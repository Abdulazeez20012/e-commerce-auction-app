from flask import current_app
from flask_pymongo import MongoClient


class MongoDBService:
    _instance = None

    def __new(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = MongoClient(current_app.config['MONGO_URI'])
            cls._instance.db = cls._instance.client.get_database()
        return cls._instance
    def get_collection(self, name):
        return self.db[name]