
class Result():
    def __init__(self):
        self._results = {
            "Flight ID" : "",
            "Departure Date" : "",
            "Departure Time" : "",
            "Departure Airport" : "",
            "Arrival Airport" : "",
            "Arrival City" : "",
            "Arrival Country" : "",
            "Price" : ""
        }

    def GetResults(self):
        return self._results