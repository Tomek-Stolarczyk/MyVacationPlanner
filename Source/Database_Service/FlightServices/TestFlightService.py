from FlightServices.IFlightService import IFlightService
import json

class TestFlightService(IFlightService):
    def GetFlightInformation(self, from_date, to_date, from_airport, to_airport):
        fp = open("TestingData/Lon+JFK.txt", "r")
        return json.load(fp)
