
class FlightData:

    def __init__(self, price, base_city, base_airport, location_city, location_airport, out_date, return_date, stop_overs, via_city):
        self.price = price
        self.base_city = base_city
        self.base_airport = base_airport
        self.location_city = location_city
        self.location_airport = location_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.via_city = via_city
