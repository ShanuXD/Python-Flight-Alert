import requests
from pprint import pprint

end_point = "https://api.sheety.co/701bd952a333c3f438672d921ce4d98a/flightDeals/users"
TOKEN = "shanu12345"

class Users:

    def __init__(self):
        self.email = ''
        self.first_name = ''
        self.last_name = ''

    def welcome_to_club(self):
        if not self.first_name:
            print("Welcome to Shanu's Flight Club!\nWe find the best deals and email you")
            print("What is your name?", end='')
            self.first_name = input()
        if not self.last_name:
            print("What is your last Name?", end='')
            self.last_name = input()
        print("What is your email?", end='')
        self.email = input()
        print("Type your email again!", end='')
        same_email = input()

        if self.email == same_email:
            print("You are in the clube!")
        else:
            print("Your email's are not matching!\nType again!")
            self.welcome_to_club()

    def save_user(self):
        user_data = {
            'user': {
                'firstName': self.first_name,
                'lastName': self.last_name,
                'email': self.email
            }
        }
        header = {
            "Authorization": f"Bearer {TOKEN}"
        }
        response = requests.post(url=end_point, headers=header, json=user_data)
        print(response.status_code)
        pprint(response.json())

    def getUsers(self):
        response = requests.get(url=end_point)
        data = response.json()['users']
        return data







