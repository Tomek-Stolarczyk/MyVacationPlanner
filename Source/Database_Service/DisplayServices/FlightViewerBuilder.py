from DatabaseServices.IDatabaseService import IDatabaseService
from FlightServices.IFlightService import IFlightService
from DisplayServices.FlightViewAdapter import FlightViewAdapter

class FlightViewerBuilder():
    def __init__(self, flight_service : IFlightService, database_service : IDatabaseService):
        self.__flight_service = flight_service
        self.__database_service = database_service
        self.__flight_views = {"Departures": [], "Returns" : []}

    def BuildOutgoingFlightView(self, from_city, destination, from_date) -> None:
        all_flights = [] 
        for from_airport in self.__database_service.GetAirportsByCity(from_city):
            for to_airport in self.__database_service.GetAirportsByCity(destination):
                from_airport_id = from_airport.Airport.AirportID
                to_airport_id = to_airport.Airport.AirportID

                all_flights.extend(self.__database_service.GetFlights(from_airport_id, to_airport_id, from_date))
        self.__flight_views["Departures"].extend([FlightViewAdapter(flight, self.__database_service) for flight in all_flights])

    def BuildReturnFlightView(self, from_city, destination, to_date) -> None:
        all_flights = []
        for from_airport in self.__database_service.GetAirportsByCity(from_city):
            for to_airport in self.__database_service.GetAirportsByCity(destination):
                from_airport_id = from_airport.Airport.AirportID
                to_airport_id = to_airport.Airport.AirportID
                all_flights.extend(self.__database_service.GetFlights(to_airport_id, from_airport_id, to_date))
        self.__flight_views["Returns"].extend([FlightViewAdapter(flight, self.__database_service) for flight in all_flights])

    def GetFlightViews(self) -> list:
        finished_flight_views = self.__flight_views
        self.__flight_views = {"Departures": [], "Returns" : []}
        return finished_flight_views