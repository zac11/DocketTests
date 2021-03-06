from faker import Faker
from config import config
import requests

# This class is responsible for generating new user objects. As well as registering the API tokens which are used in
# the tests.

class Generate(object):
    def __init__(self):
        fake = Faker()

        self.user = {
            "Username": fake.name().split(' ', 1)[0],
            "Email Address": fake.email(),
            "Password": fake.word(),
            "Todo": fake.word()
        }

    def GetUser(self):
        new_user = self.user
        return new_user

    def GetToken(self):
        token = requests.post(config.SERVER + '/api/Register/',
                              json={'Username': self.user["Username"],'Email Address': self.user["Email Address"],
                                    'Password': self.user["Password"]}).text.split()[-1][:-2]
        return token




