class BasicFlightData():
    def __init__(self):
        self._flight_data = {
            'Fly From' : "",
            'Fly To' : "",
            'cityFrom': "",
            'cityTo': "",
            'countryFrom': "",
            'countryTo': "",
            'price' : ""
        }

    def GetSimpleFlightData(self):
        return self._flight_data

class BasicFlightDataAdapter(BasicFlightData):
    def __init__(self, verbose_flight_data : dict):
        new_flights = []
        for flight_data in verbose_flight_data['data']:
            new_flights.append({
                               'flyFrom' : flight_data['flyFrom'],
                               'flyTo' : flight_data['flyTo'],
                               'cityFrom': flight_data['cityFrom'],
                               'cityTo': flight_data['cityTo'],
                               'countryFrom': flight_data['countryFrom']['name'],
                               'countryTo': flight_data['countryTo']['name'],
                               'price': flight_data['price']
                               })
        self._flight_data = new_flights
    
    def GetSimpleFlightData(self):
        return self._flight_data
        
