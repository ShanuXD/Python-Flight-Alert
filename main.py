from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
from users import Users


base_city_iata = "BLR" #Banglore

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
users = Users()
sheet_data = data_manager.get_data()

# pprint(sheet_data)

if sheet_data[0]['iataCode'] == ' ':
    for location in sheet_data:
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

        msg = f"Low Price Alert!!! Only Rs.{flight.price} to fly from {flight.base_city}-{flight.base_airport} to {flight.location_city}-{flight.location_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            msg += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        # notification_manager.sendMsg(msg)
        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.base_airport}.{flight.location_airport}.{flight.out_date}*{flight.location_airport}.{flight.base_airport}.{flight.return_date}"

        all_users_data = users.getUsers()
        # print(all_users_data)
        for user in all_users_data:
            user_email = user['email']
            notification_manager.sendMail(msg, user_email, link)








        
        




