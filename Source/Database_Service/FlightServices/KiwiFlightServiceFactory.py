from FlightServices.IFlightService import IFlightService
from FlightServices.KiwiFlightService import KiwiFlightService
from FlightServices.FlightServicesFactoryMethod import FlightServicesFactoryMethod

# Concrete implementation of the abstract factory
class KiwiFlightServiceFactory(FlightServicesFactoryMethod):
    def CreateFlightServices() -> IFlightService:
        return KiwiFlightService() 