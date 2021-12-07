from abc import ABC, abstractclassmethod
from FlightServices.IFlightService import IFlightService

# Abstract factory for creating Flight Services
class FlightServicesFactoryMethod(ABC):
    @abstractclassmethod
    def CreateFlightServices() -> IFlightService:
        pass