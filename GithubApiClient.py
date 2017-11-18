from urllib.request import urlopen

import json


class GithubApiClient:
    endpoints = {"user": "users/", "search": "search/"}

    def __init__(self, client_id, client_secret):
        self.base_url = "https://api.github.com/"
        self.client_id = client_id
        self.client_secret = client_secret

    def public_api_call(self, endpoint, parameters):
        url = self.base_url + endpoint + parameters
        result = urlopen(url).read()
        return json.loads(result)

    def private_api_call(self, endpoint, parameters):
        url = self.base_url + endpoint + parameters + \
              "?client_id=" + self.client_id + \
              "&client_secret=" + self.client_secret
        result = urlopen(url).read()
        return json.loads(result)
