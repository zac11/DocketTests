import requests
from config import config


class sampleauth:
    def __init__(self):
        self.url = config.SERVER + '/api/path1/'

    def authtests(self, user):
        # I want to use this token from the FE page
        token = "hard-coded-token"
        query = {"search":"name"}
        # A request is then made to delete the user to reset the server back to its initial state
        result = requests.get(url=self.url, headers={"Authorization":"Bearer %s" % token,
                                                     "Content-Type":"application/json"},
                              params=query)

        return result
