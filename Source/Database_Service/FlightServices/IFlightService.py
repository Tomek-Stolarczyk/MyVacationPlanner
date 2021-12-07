from abc import ABC, abstractmethod
from datetime import datetime
import json

# The basic methods that all flight services should implement
class IFlightService(ABC):
    @abstractmethod
    def GetFlightInformation(self, from_date : datetime, to_date : datetime, from_airport : str, to_airport : str) -> json:
        pass

    @abstractmethod
    def GetAirportsAroundCity(self, city : str) -> json:
        pass

    @abstractmethod
    def GetDestinationLessFlights(self, from_date : datetime, to_date : datetime, from_airport : str) -> json:
        pass