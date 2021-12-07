from FlightServices.IFlightService import IFlightService
import json
import requests
import urllib
import datetime

# The Kiwi Flight Service class uses the kiwi api to query live databases for flights
# We hardcode some fields such as limit and currency, but the important one is apikey.
# The apikey allows us to authenticate with the api service and get the requested flight
# data. We usually return the json data that accompanies the request, allowing other
# classes to handle
class KiwiFlightService(IFlightService):
    def __init__(self):
         self.__url = "https://tequila-api.kiwi.com"
         self.__headers = { 'apikey': "xbApFCudJlUMZySrKoSITBYxIy6nMP1m" }

    def GetFlightInformation(self, from_date : datetime, to_date : datetime, from_airport : str, to_airport : str) -> json:
        from_date = from_date.split('-')[2] + "/" + from_date.split('-')[1]+ "/"+ from_date.split('-')[0]
        to_date = to_date.split('-')[2] + "/" + to_date.split('-')[1]+ "/"+ to_date.split('-')[0]

        flight_info = {"fly_from" : f"airport:{from_airport}",
                       "fly_to" : f"airport:{to_airport}",
                       "date_from" : from_date,
                       "date_to" : from_date,
                       "return_from" : to_date,
                       "return_to" : to_date,
                       "max_stopovers" : 1,
                       "flight_type" : "round",
                       "curr" : "USD",
                       "vehicle_type" : "aircraft",
                       "limit" : "10"}
        url = self.__url + "/v2/search?" + urllib.parse.urlencode(flight_info)

        response = requests.request("GET", url, headers=self.__headers)
        assert(response.status_code == 200)
        return json.loads(response.content)

    # When we eventually find a city to fly to, we want to see if there are
    # more than 1 airport per city. Return any that the api finds.
    def GetAirportsAroundCity(self, city : str) -> json:
        info = {
                "term" : f"{city}",
                "locale" : "en-US",
                "location_types" : "airport",
                "limit" : "10"}
        url = self.__url + "/locations/query?" + urllib.parse.urlencode(info)
        response = requests.request("GET", url, headers=self.__headers)
        assert(response.status_code == 200)
        return json.loads(response.content)

    # This method is mainly used by the periodic scanner when it probes the api for new airports and stores flights
    def GetDestinationLessFlights(self, from_date : datetime, to_date : datetime, from_airport : str) -> json:
        from_date = from_date.split('-')[2] + "/" + from_date.split('-')[1]+ "/"+ from_date.split('-')[0]
        to_date = to_date.split('-')[2] + "/" + to_date.split('-')[1]+ "/"+ to_date.split('-')[0]

        flight_info = {"fly_from" : f"airport:{from_airport}",
                       "date_from" : from_date,
                       "date_to" : from_date,
                       "return_from" : to_date,
                       "return_to" : to_date,
                       "flight_type" : "round",
                       "max_stopovers" : 1,
                       "curr" : "USD",
                       "vehicle_type" : "aircraft",
                       "limit" : "10"}
        url = self.__url + "/v2/search?" + urllib.parse.urlencode(flight_info)

        response = requests.request("GET", url, headers=self.__headers)
        assert(response.status_code == 200)
        return json.loads(response.content)