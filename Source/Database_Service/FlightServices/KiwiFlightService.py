from FlightServices.IFlightService import IFlightService
import json
import requests
import urllib

class KiwiFlightService(IFlightService):
    def __init__(self):
         self.url = "https://tequila-api.kiwi.com"
         self.headers = { 'apikey': "xbApFCudJlUMZySrKoSITBYxIy6nMP1m" }

    def GetFlightInformation(self, from_date, to_date, from_airport, to_airport):
        from_date = from_date.split('-')[2] + "/" + from_date.split('-')[1]+ "/"+ from_date.split('-')[0]
        to_date = to_date.split('-')[2] + "/" + to_date.split('-')[1]+ "/"+ to_date.split('-')[0]

        flight_info = {"fly_from" : f"airport:{from_airport}",
                       "fly_to" : f"airport:{to_airport}",
                       "date_from" : from_date,
                       "date_to" : from_date,
                       "return_from" : to_date,
                       "return_to" : to_date,
                       "flight_type" : "round",
                       "Curr" : "USD",
                       "vehicle_type" : "aircraft",
                       "limit" : "10"}
        url = self.url + "/v2/search?" + urllib.parse.urlencode(flight_info)

        response = requests.request("GET", url, headers=self.headers)
        assert(response.status_code == 200)
        return json.loads(response.content)

    def GetAirportsAroundCity(self, city : str) -> json:
        info = {
                "term" : f"{city}",
                "locale" : "en-US",
                "location_types" : "airport",
                "limit" : "10"}
        url = self.url + "/locations/query?" + urllib.parse.urlencode(info)
        response = requests.request("GET", url, headers=self.headers)
        assert(response.status_code == 200)
        return json.loads(response.content)

    def GetDestinationLessFlights(self, from_date, to_date, from_airport):
        from_date = from_date.split('-')[2] + "/" + from_date.split('-')[1]+ "/"+ from_date.split('-')[0]
        to_date = to_date.split('-')[2] + "/" + to_date.split('-')[1]+ "/"+ to_date.split('-')[0]

        flight_info = {"fly_from" : f"airport:{from_airport}",
                       "date_from" : from_date,
                       "date_to" : from_date,
                       "return_from" : to_date,
                       "return_to" : to_date,
                       "flight_type" : "round",
                       "Curr" : "USD",
                       "vehicle_type" : "aircraft",
                       "limit" : "10"}
        url = self.url + "/v2/search?" + urllib.parse.urlencode(flight_info)

        response = requests.request("GET", url, headers=self.headers)
        assert(response.status_code == 200)
        return json.loads(response.content)