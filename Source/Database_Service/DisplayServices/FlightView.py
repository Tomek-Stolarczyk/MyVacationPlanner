from DisplayServices.View import View
import datetime

# Create a view for locations. This is usually an airport
class LocationView(View):
    def __init__(self, airport_id : str, city : str, country : str, state = ""):
        self.__location_view = {
            "Airport ID" : airport_id,
            "City" : city,
            "State" : state,
            "Country" : country
        }

    # When printing a table in html, these are expected to be in the header
    def GetViewTableHeaders(self) -> list:
        return ["City", "State", "Country", "Airport Code"]

    def GetViewTableRow(self) -> list:
        return [self.__location_view["City"], self.__location_view["State"], self.__location_view["Country"], self.__location_view["Airport ID"]]
    
    def GetViewID(self) -> str:
        return self.__location_view["Airport ID"]

class FlightView(View):
    def __init__(self):
        self.__flight_view = {
            "Flight ID" : "",
            "Departure Date" : "",
            "Departure Time" : "",
            "Departure Location" : None,
            "Arrival Location" : None,
            "Price" : ""
        }
    
    # When printing a table in html, these are expected to be in the header
    def GetViewTableHeaders(self) -> list:
        departure_data = ["Departure " + data for data in self.__flight_view["Departure Location"].GetViewTableHeaders()]
        arrival_data = ["Arrival " + data for data in self.__flight_view["Arrival Location"].GetViewTableHeaders()]
        return ["Departure Date", "Departure Time"] + departure_data + arrival_data + ["Price"]

    # When printing a table in html, this method returns a row that correlates
    # with the object
    def GetViewTableRow(self) -> list:
        departure_data = self.__flight_view["Departure Location"].GetViewTableRow()
        arrival_data = self.__flight_view["Arrival Location"].GetViewTableRow()
        return [self.__flight_view["Departure Date"], self.__flight_view["Departure Time"]] + departure_data + arrival_data + [self.__flight_view["Price"]]

    def SetFlightInfo(self, flight_id : str, departure_date_time : datetime, departure_location : LocationView, arrival_location : LocationView, price : float) -> None:
        self.__flight_view["Flight ID"] = flight_id
        self.__flight_view["Departure Date"] = str(departure_date_time.date())
        self.__flight_view["Departure Time"] = str(departure_date_time.time())
        self.__flight_view["Arrival Location"] = arrival_location
        self.__flight_view["Departure Location"] = departure_location
        self.__flight_view["Price"] = str(price) + " USD"

    def GetViewID(self) -> str:
        return self.__flight_view["Flight ID"]


