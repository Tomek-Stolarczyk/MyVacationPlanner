from abc import ABC, abstractclassmethod

class IFlightService(ABC):
    @abstractclassmethod
    def GetFlightInformation(self, from_date, to_date, from_airport, to_airport):
        pass