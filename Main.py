from Users import GetUsers

if __name__ == "__main__":
    user_list = GetUsers.DownloadUsers.download_users("repositories?q=java&sort=stars&order=desc")
    for user in user_list:
        print str(user)
        user.save_user()
