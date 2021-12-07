from DatabaseServices.IDatabaseService import IDatabaseService
from FlightServices.IFlightService import IFlightService
from DisplayServices.FlightViewAdapter import FlightViewAdapter
import datetime

class FlightViewerBuilder():
    def __init__(self, flight_service : IFlightService, database_service : IDatabaseService):
        self.__flight_service = flight_service
        self.__database_service = database_service
        self.__flight_views = {"Round Trip": []}

    # Get flights that are associated with the search from the database, throw them into the
    # flight_views object to be returned later
    def BuildFlightView(self, from_city : str, destination : str, from_date : datetime) -> None:
        all_flights = [] 
        for from_airport in self.__database_service.GetAirportsByCity(from_city):
            for to_airport in self.__database_service.GetAirportsByCity(destination):
                from_airport_id = from_airport.Airport.AirportID
                to_airport_id = to_airport.Airport.AirportID

                all_flights.extend(self.__database_service.GetFlights(from_airport_id, to_airport_id, from_date))
        self.__flight_views["Round Trip"] = [FlightViewAdapter(flight, self.__database_service) for flight in all_flights]
        assert(len(self.__flight_views["Round Trip"]) == len(all_flights))

    # Go into the flight service and attempt to grab some new data for the flights. This should refresh
    # some of the existing data in the database and prime us for grabbing soon
    def SeedWithLiveData(self, from_city : str, destination : str, from_date : datetime, to_date : datetime) -> None:
        for from_airport in self.__database_service.GetAirportsByCity(from_city):
            for to_airport in self.__database_service.GetAirportsByCity(destination):
                live_data = self.__flight_service.GetFlightInformation(str(from_date.strftime("%Y-%m-%d")), str(to_date.strftime("%Y-%m-%d")), from_airport.Airport.AirportID, to_airport.Airport.AirportID)
                if(live_data['data'] is not None):
                    for raw_flight in live_data['data']:
                        self.__database_service.AddFlightFromRaw(raw_flight)

    # Now that the object has been completed, return it and reset the existing flight views
    def GetFlightViews(self) -> dict:
        finished_flight_views = self.__flight_views
        self.__flight_views = {"Round Trip": []}
        return finished_flight_views