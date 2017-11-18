import pymongo
from pymongo import MongoClient


class MongoController:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)

    def connect_database(self):
        db = self.client.web_crawler
        collection = db.users
        user = {"name": "David",
                "login": "Daviddfa",
                "email": "david@gmail.com",
                "location": "Vilagrassa",
                "avatar_url": "google.es"}

        post_id = collection.insert_one(user).inserted_id
        print post_id