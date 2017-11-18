from Users import DownloadUsers
from DatabaseController import MongoController

if __name__ == "__main__":

    user_list = DownloadUsers.DownloadUsers.download_users("repositories?q=java&sort=stars&order=desc")
    print len(user_list)
    for user in user_list:
        print str(user)
        user.save_user()
