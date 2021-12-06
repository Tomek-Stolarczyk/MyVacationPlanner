from DatabaseServices.IDatabaseService import IDatabaseService
from FlightServices.IFlightService import IFlightService
import time, threading
from datetime import datetime, timedelta
import random
import json

g_periodic_updater = None

def GetPeriodicUpdater(flight_service : IFlightService, database_service : IDatabaseService):
    global g_periodic_updater
    if g_periodic_updater == None:
        g_periodic_updater = PeriodicUpdater(flight_service, database_service)
    return g_periodic_updater

class PeriodicUpdater(threading.Thread):
    def __init__(self, flight_service : IFlightService, database_service : IDatabaseService):
        threading.Thread.__init__(self)
        self.__stopped = threading.Event()
        self.__interval = 20
        self.__flight_service = flight_service
        self.__database_service = database_service

    def stop(self):
        self.__stopped.set()
        self.join()

    def run(self):
            while not self.__stopped.wait(self.__interval):
                self.LookForNewData()

    def LookForNewData(self):
        starting_airport = self.__database_service.GetRandomAirport().Airport.AirportID
        starting_day = datetime.now() + timedelta(days=random.randint(0,100))
        return_day = starting_day + timedelta(days=random.randint(10,40))
        raw_flights = self.__flight_service.GetDestinationLessFlights(
                                    str(starting_day).split(' ')[0],
                                    str(return_day).split(' ')[0],
                                    starting_airport)
        flights = []
        for raw_flight in raw_flights['data']:
            if(len(self.__database_service.GetAirportByID(raw_flight['flyTo'])) == 0):
                airports = self.__flight_service.GetAirportsAroundCity(raw_flight['cityTo'])
                for raw_airport in airports['locations']:
                    self.__database_service.AddAirportFromRaw(raw_airport)
            self.__database_service.AddFlightFromRaw(raw_flight)
        

    