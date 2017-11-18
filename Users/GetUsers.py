from GithubApiClient import GithubApiClient
from Users import User


class GetUsers:
    gac = GithubApiClient("abce3e0cd57466d1d55c", "ccfdf4e7e7b36d1aca21a43f5d381a55c9c4e084")

    @staticmethod
    def get_user(login):
        user = GetUsers.gac.private_api_call(GithubApiClient.endpoints["user"], login)
        return User.User(user["name"], user["login"], user["email"], user["location"], user["avatar_url"])

    @staticmethod
    def download_users(search_prefs):
        users = GetUsers.gac.public_api_call(GithubApiClient.endpoints["search"], search_prefs)
        user_list = []
        for user in users['items']:
            login = user["owner"]["login"]
            user_list.append(GetUsers.get_user(login))

        return user_list
