class Flight:
    def __init__(self, f_id, f_city, t_city, cost):
        self.f_id = f_id
        self.f_city = f_city
        self.t_city = t_city
        self.cost = cost

class FlightTable:
    def __init__(self):
        self.flights = []
    
    
    def search_by_city(self, city):
        result = []
        for flight in self.flights:
            if flight.t_city == city:
                result.append(flight)
        return result
    
    def search_between_cities(self, f_city, t_city):
        result = []
        for flight in self.flights:
            if flight.f_city == f_city and flight.t_city == t_city:
                result.append(flight)
        return result
    
    def search_from_city(self, city):
        result = []
        for flight in self.flights:
            if flight.f_city == city:
                result.append(flight)
        return result

    def add_flight(self, flight):
        self.flights.append(flight)
    
    

flight_table = FlightTable()
flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))
flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))


sp = int(input("Enter search parameter (1: Flights for a particular City, 2: Flights From a city, 3: Flights between two given cities): "))
if sp == 1:
    city = input("Enter city: ")
    result = flight_table.search_by_city(city)
elif sp == 2:
    city = input("Enter from city: ")
    result = flight_table.search_from_city(city)
elif sp == 3:
    from_city = input("Enter from city: ")
    to_city = input("Enter to city: ")
    result = flight_table.search_between_cities(from_city, to_city)
if (len(result)!=0):
    for flight in result:
        print(f"Flight ID: {flight.f_id}, From: {flight.f_city}, To: {flight.t_city}, Price: {flight.cost}")
else:
    print("No flights between cities.")
