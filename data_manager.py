import requests

endpoint = "-------------Your Sheety endpoint!----------------"

class DataManager:

    def __init__(self):
        self.location_data = {}

    def get_data(self):
        response = requests.get(url=endpoint)
        data = response.json()
        print(data)
        self.location_data = data["sheet1"]
        return self.location_data

    def updateLocationData(self):

        for city in self.location_data:
            update_data = {
                "sheet1": {"iataCode": city["iataCode"]}
            }
            response = requests.put(url=f"{endpoint}/{city['id']}", json=update_data)
            # print(response.status_code)
