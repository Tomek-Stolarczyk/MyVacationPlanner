from FlightServices.IFlightService import IFlightService
import json
import datetime

# Test class implementation of the flight service - useful for offline testing
class TestFlightService(IFlightService):
    def GetFlightInformation(self, from_date : datetime, to_date : datetime, from_airport : str, to_airport : str) -> json:
        fp = open("TestingData/Lon+JFK.txt", "r")
        return json.load(fp)

    def GetAirportsAroundCity(self, city : str) -> json:
        return json.loads("")

    def GetDestinationLessFlights(self, from_date : datetime, to_date : datetime, from_airport : str) -> json:
        return json.loads("")