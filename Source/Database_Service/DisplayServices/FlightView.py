class LocationView():
    def __init__(self, airport_id : str, city : str, country : str, state = ""):
        self.__location_view = {
            "Airport ID" : airport_id,
            "City" : city,
            "State" : state,
            "Country" : country
        }
    
    def __str__(self):
        print("Invoking string representation of location")
        return "City: {}" % self.__location_view["City"]

    def GetViewTableHeaders(self):
        return ["City", "State", "Country", "Airport Code"]

    def GetViewTableRow(self):
        return [self.__location_view["City"], self.__location_view["State"], self.__location_view["Country"], self.__location_view["Airport ID"]]

class FlightView():
    def __init__(self):
        self.__flight_view = {
            "Flight ID" : "",
            "Departure Date" : "",
            "Departure Time" : "",
            "Departure Location" : None,
            "Arrival Location" : None,
            "Price" : ""
        }
    
    def GetViewTableHeaders(self):
        departure_data = ["Departure " + data for data in self.__flight_view["Departure Location"].GetViewTableHeaders()]
        arrival_data = ["Arrival " + data for data in self.__flight_view["Arrival Location"].GetViewTableHeaders()]
        return ["Departure Date", "Departure Time"] + departure_data + arrival_data + ["Price"]

    def GetViewTableRow(self):
        departure_data = self.__flight_view["Departure Location"].GetViewTableRow()
        arrival_data = self.__flight_view["Arrival Location"].GetViewTableRow()
        return [self.__flight_view["Departure Date"], self.__flight_view["Departure Time"]] + departure_data + arrival_data + [self.__flight_view["Price"]]

    def SetFlightInfo(self, flight_id, departure_date_time, departure_location, arrival_location, price):
        self.__flight_view["Flight ID"] = flight_id
        self.__flight_view["Departure Date"] = str(departure_date_time)
        self.__flight_view["Departure Time"] = "9:00am"
        self.__flight_view["Arrival Location"] = arrival_location
        self.__flight_view["Departure Location"] = departure_location
        self.__flight_view["Price"] = str(price) + " USD"

    def GetViewID(self):
        return self.__flight_view["Flight ID"]


