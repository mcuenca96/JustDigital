from GithubApiClient import GithubApiClient
from Users.GetUsers import GetUsers


class GetFollowers:
    @staticmethod
    def get_followers(user_login):
        gac = GithubApiClient("abce3e0cd57466d1d55c", "ccfdf4e7e7b36d1aca21a43f5d381a55c9c4e084")

        followers = gac.private_api_call(GithubApiClient.endpoints["user"], "followers/" + user_login)

        followers_list = []
        for follower in followers:
            login = follower["login"]
            user = GetUsers.get_user(login)

            followers_list.append(user)

        return followers_list
