from abc import ABC, abstractclassmethod
from DatabaseServices.Database_Schema import Airport, Flight
import json
import datetime

# Database class which needs to be made concrete. These methods
# are used throughout the vacation planner. If a method is missing,
# this violates further assumptions in the codebase. Methods are 
# self documenting
class IDatabaseService(ABC):
    @abstractclassmethod
    def AddAirport(self, airport : Airport) -> None:
        pass

    @abstractclassmethod
    def AddFlight(self, flight : Flight) -> None:
        pass

    @abstractclassmethod
    def AddFlightFromRaw(self, raw_flight : json) -> None:
        pass

    @abstractclassmethod
    def AddAirportFromRaw(self, raw_airport : json) -> None:
        pass

    @abstractclassmethod
    def GetAirportsByContinent(self, continent : str) -> list:
        pass

    @abstractclassmethod
    def GetAirportsByCountry(self, country : str) -> list:
        pass

    @abstractclassmethod
    def GetAirportsByCity(self, city : str) -> list:
        pass
    
    @abstractclassmethod
    def GetAirportByID(self, airportID : str) -> list:
        pass
    
    @abstractclassmethod
    def GetAllAirports(self) -> list:
        pass

    @abstractclassmethod
    def GetAllFlights(self) -> list:
        pass

    @abstractclassmethod
    def GetFlights(self, from_airport : str, to_airport : str, departure_date : datetime, limit=10) -> list:
        pass

    @abstractclassmethod
    def GetRandomAirport(self) -> list:
        pass

    @abstractclassmethod
    def GetFlightByID(self, flight_id : str) -> list:
        pass