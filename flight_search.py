import requests
from flight_data import FlightData
from pprint import pprint

# Tequila endpoint and Api
location_endpoint = "https://tequila-api.kiwi.com"
location_api = "--------------Tequila Api-----------------"


class FlightSearch:

    def getIataCode(self, city_name):
        endpoint = f"{location_endpoint}/locations/query"
        headers = {"apikey": location_api}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=endpoint, params=query, headers=headers)
        location_data = response.json()["locations"]
        return location_data[0]["code"]

    def checkFlights(self, base_city_code, location_code, from_time, to_time):
        header = {"apikey": location_api}
        query = {
            "fly_from": base_city_code,
            "fly_to": location_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=f"{location_endpoint}/v2/search", params=query, headers=header)
        data = response.json()["data"]
        if data:
            # pprint(data)
            data = data[0]
            flight_data = FlightData(
                price=data['price'],
                base_city=data["route"][0]["cityFrom"],
                base_airport=data["route"][0]["flyFrom"],
                location_city=data["route"][0]["cityTo"],
                location_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            print(f"{flight_data.location_city}: £{flight_data.price}")
            return flight_data

        return False

