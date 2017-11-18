from Users import DownloadUsers
from DatabaseController import MongoController
if __name__ == "__main__":
    db = MongoController.MongoController()
    db.connect_database()

    for user in DownloadUsers.DownloadUsers.download_users("repositories?q=java&sort=stars&order=desc"):
       print(str(user) + "\n")

