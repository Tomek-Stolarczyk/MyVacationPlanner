from FlightServices.IFlightService import IFlightService
from FlightServices.KiwiFlightService import KiwiFlightService
from FlightServices.FlightServicesFactoryMethod import FlightServicesFactoryMethod

class KiwiFlightServiceFactory(FlightServicesFactoryMethod):
    def CreateFlightServices() -> IFlightService:
        return KiwiFlightService() 