from flask import render_template, request, redirect
# from FlightServices.TestFlightServiceFactory import TestFlightServiceFactory as FlightServiceFactory
from FlightServices.KiwiFlightServiceFactory import KiwiFlightServiceFactory as FlightServiceFactory
from DatabaseServices.PostgresDatabaseServiceFactory import PostgresDatabaseServiceFactory as DatabaseServiceFactory
# from FlightServiceAdapter import BasicFlightDataAdapter
from DatabaseServices.Database_Schema import Airport
from PeriodicUpdater import GetPeriodicUpdater

class VacationPlannerFacade():
    def __init__(self):
        self.flight_service = FlightServiceFactory.CreateFlightServices()
        self.database_service = DatabaseServiceFactory.CreateDatabaseService()
        self.periodic_updator = GetPeriodicUpdater(self.flight_service, DatabaseServiceFactory.CreateDatabaseService())
        self.periodic_updator.start()

    def ListFlights(self):
        flights = self.database_service.GetAllFlights()
        return render_template('ListFlights.html', flights=flights)

    def ListAirports(self):
        airports = self.database_service.GetAllAirports()
        return render_template('ListAirports.html', airports=airports)

    def LoadAirportsIntoDatabase(self, airports):
        for airport_raw in airports['locations']:
            self.database_service.AddAirportFromRaw(airport_raw)

    def GetClosestAirportToCity(self, city : str) -> str:
        database_airports = self.database_service.GetAirportsByCity(city)
        if(len(database_airports) == 0):
            airports = self.flight_service.GetAirportsAroundCity(city)
            self.LoadAirportsIntoDatabase(airports)
        
        database_airports = self.database_service.GetAirportsByCity(city)
        return database_airports[0].Airport.AirportID


    def GetAirportsInCountry(self, country : str):
        return self.database_service.GetAirportsByCountry(country)

    def GetAirportsInContinent(self, continent : str):
        return self.database_service.GetAirportsByContinent(continent)

    def SearchResults(self):
        from_city = request.form['From City']
        from_date = request.form['Depart Date']
        to_date = request.form['Return Date']
        destination_type = request.form['Destination Type']
        destination = request.form['Destination']
                      
        if(destination_type == "Continent"):
            refine_destination = "Country"
            to_airports = self.database_service.GetAirportsByContinent(destination)
            to_destinations = sorted(set([airport.Airport.Country for airport in to_airports]))
        elif(destination_type == "Country"):
            refine_destination = "City"
            to_airports = self.database_service.GetAirportsByCountry(destination)
            to_destinations = sorted(set([airport.Airport.City for airport in to_airports]))
        elif(destination_type == "Any"):
            refine_destination = "Continent"
            to_airports = self.database_service.GetAllAirports()
            to_destinations = sorted(set([airport.Airport.Continent for airport in to_airports]))
        else: # destination_type == "City"
            refine_destination = None
            to_airports = self.database_service.GetAirportsByCity(destination)
            to_destinations = sorted(set([airport.Airport.Continent for airport in to_airports]))
        

        # TODO: Send to Database
        # verbose_results = self.FlightService.GetFlightInformation(from_date, to_date, from_airport, to_airports[0].Airport.AirportID)
        # basic_results = BasicFlightDataAdapter(verbose_results)
        # return render_template('/SearchResults.html', 
        #                         search_criteria=request.form, 
        #                         results=basic_results.GetSimpleFlightData())

        if(refine_destination is None):
            flights = self.GetAvailableFlights(from_city, destination, from_date, to_date)
            return render_template('/SearchResults.html', search_criteria=request.form, results=flights)
        else:
            return render_template('/DestinationSelection.html', search_criteria=request.form, destinations=to_destinations, destination_type=refine_destination)

    def HomePage(self):
        return render_template('Home.html')

    def GetAvailableFlights(self, from_city, to_city, from_date, to_date):
        all_flights = []
        for from_airport in self.database_service.GetAirportsByCity(from_city):
            for to_airport in self.database_service.GetAirportsByCity(to_city):
                all_flights.extend(self.database_service.GetFlights(from_airport, to_airport, from_date))
                all_flights.extend(self.database_service.GetFlights(from_airport, to_airport, to_date))
        return all_flights
        