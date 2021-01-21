from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager


base_city_iata = "BLR" #Banglore

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_data()

pprint(sheet_data)

for location in sheet_data:
    if not location['iataCode']:
        city_name = location['city']
        location["iataCode"] = flight_search.getIataCode(city_name)
    data_manager.location_data = sheet_data
    data_manager.updateLocationData()


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for location in sheet_data:
    flight = flight_search.checkFlights(base_city_iata, location['iataCode'], from_time=tomorrow, to_time=six_month_from_today)

    if not flight:
        continue
    if flight.price < location['lowestPrice']:

        msg = f"Low Price Alert!!! Only £{flight.price} to fly from {flight.base_city}-{flight.base_airport} to {flight.location_city}-{flight.location_airport}, from {flight.out_date} to {flight.return_date}."

        notification_manager.sendMsg(msg)



        
        




