from DisplayServices.FlightView import FlightView, LocationView
from DisplayServices.View import View
from DatabaseServices.Database_Schema import Airport

# This class converts between a database Flight object and a FlightView
# It allows the builder to work consistently with views and easily convert
class FlightViewAdapter(View):
    def __init__(self, database_flight, database_service):
        self.__internal_flight = FlightView()
        self.__database_service = database_service
        airport_from = self.__database_service.GetAirportByID(database_flight.Flight.AirportFrom)[0]
        airport_to = self.__database_service.GetAirportByID(database_flight.Flight.AirportTo)[0]
        
        self.__internal_flight.SetFlightInfo(database_flight.Flight.FlightID,
                                            database_flight.Flight.Date,
                                            self.CreateLocationFromAirport(airport_from),
                                            self.CreateLocationFromAirport(airport_to),
                                            database_flight.Flight.Price)

    def CreateLocationFromAirport(self, airport : Airport) -> LocationView:
        return LocationView(airport.Airport.AirportID,
                                airport.Airport.City,
                                airport.Airport.Country,
                                state=airport.Airport.State)

    def GetViewTableHeaders(self) -> list:
        return self.__internal_flight.GetViewTableHeaders()
    
    def GetViewTableRow(self) -> list:
        return self.__internal_flight.GetViewTableRow()

    def GetViewID(self) -> str:
        return self.__internal_flight.GetViewID()

