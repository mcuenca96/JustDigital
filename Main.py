from Users import DownloadUsers

if __name__ == "__main__":
    for user in DownloadUsers.DownloadUsers.download_users("repositories?q=java&sort=stars&order=desc"):
        print(str(user) + "\n")