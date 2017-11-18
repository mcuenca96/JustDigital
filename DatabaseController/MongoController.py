from pymongo import MongoClient


class MongoController:
    __controller = None

    def __init__(self):
        self.client = MongoClient('localhost', 27017)

    @staticmethod
    def get_instance():
        if not MongoController.__controller:
            MongoController.__controller = MongoController()

        return MongoController.__controller

    def save_user(self, user):
        db = self.client.web_crawler
        collection = db.users

        # Check if exists
        if collection.find_one({"login": user["login"]}):
            print "Already exists"
            return

        collection.insert_one(user)
