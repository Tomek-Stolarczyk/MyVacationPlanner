from abc import ABC, abstractclassmethod
from DatabaseServices.Database_Schema import Airport, Flight

class IDatabaseService(ABC):
    @abstractclassmethod
    def AddAirport(self, airport : Airport):
        pass

    @abstractclassmethod
    def AddFlight(self, flight : Flight):
        pass

    @abstractclassmethod
    def GetAirportsByContinent(self, continent : str):
        pass

    @abstractclassmethod
    def GetAirportsByCountry(self, country : str):
        pass

    @abstractclassmethod
    def GetAirportsByCity(self, city : str):
        pass