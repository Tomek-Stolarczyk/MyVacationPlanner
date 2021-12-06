from FlightServices.IFlightService import IFlightService
from FlightServices.TestFlightService import TestFlightService
from FlightServices.FlightServicesFactoryMethod import FlightServicesFactoryMethod

class TestFlightServiceFactory(FlightServicesFactoryMethod):
    def CreateFlightServices() -> IFlightService:
        return TestFlightService() 