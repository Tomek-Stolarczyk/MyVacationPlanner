from abc import ABC, abstractclassmethod
from FlightServices.IFlightService import IFlightService

class FlightServicesFactoryMethod(ABC):
    @abstractclassmethod
    def CreateFlightServices() -> IFlightService:
        pass