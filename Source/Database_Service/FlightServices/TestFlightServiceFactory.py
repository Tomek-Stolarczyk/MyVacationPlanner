from FlightServices.IFlightService import IFlightService
from FlightServices.TestFlightService import TestFlightService
from FlightServices.FlightServicesFactoryMethod import FlightServicesFactoryMethod

# Concrete implementation of abstract factory. Used to create the testing flight service
class TestFlightServiceFactory(FlightServicesFactoryMethod):
    def CreateFlightServices() -> IFlightService:
        return TestFlightService() 