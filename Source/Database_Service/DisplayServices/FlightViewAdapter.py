from DisplayServices.FlightView import FlightView, LocationView

class FlightViewAdapter(FlightView):
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

    def CreateLocationFromAirport(self, airport):
        return LocationView(airport.Airport.AirportID,
                                airport.Airport.City,
                                airport.Airport.Country,
                                state=airport.Airport.State)

    def GetViewTableHeaders(self):
        return self.__internal_flight.GetViewTableHeaders()
    
    def GetViewTableRow(self):
        return self.__internal_flight.GetViewTableRow()

    def GetViewID(self):
        return self.__internal_flight.GetViewID()

