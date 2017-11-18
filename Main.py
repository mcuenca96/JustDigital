from Users import DownloadUsers

if __name__ == "__main__":
    user_list = DownloadUsers.DownloadUsers.download_users("repositories?q=java&sort=stars&order=desc")
    for user in user_list:
        print(str(user) + "\n"

