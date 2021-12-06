from flask import render_template, request, redirect
# from FlightServices.TestFlightServiceFactory import TestFlightServiceFactory as FlightServiceFactory
from FlightServices.KiwiFlightServiceFactory import KiwiFlightServiceFactory as FlightServiceFactory
from DatabaseServices.PostgresDatabaseServiceFactory import PostgresDatabaseServiceFactory as DatabaseServiceFactory
# from FlightServiceAdapter import BasicFlightDataAdapter
from DatabaseServices.Database_Schema import Airport
from PeriodicUpdater import GetPeriodicUpdater
from DisplayServices.FlightViewerBuilder import FlightViewerBuilder
import json
from datetime import datetime

class VacationPlannerFacade():
    def __init__(self):
        self.flight_service = FlightServiceFactory.CreateFlightServices()
        self.__database_service = DatabaseServiceFactory.CreateDatabaseService()
        self.periodic_updator = GetPeriodicUpdater(self.flight_service, DatabaseServiceFactory.CreateDatabaseService())
        # self.periodic_updator.start()
        self.__flight_viewer = FlightViewerBuilder(self.flight_service, self.__database_service)

    def ListFlights(self):
        flights = self.__database_service.GetAllFlights()
        return render_template('ListFlights.html', flights=flights)

    def ListAirports(self):
        airports = self.__database_service.GetAllAirports()
        return render_template('ListAirports.html', airports=airports)

    def LoadAirportsIntoDatabase(self, airports : json):
        for airport_raw in airports['locations']:
            self.__database_service.AddAirportFromRaw(airport_raw)

    def GetClosestAirportToCity(self, city : str) -> str:
        database_airports = self.__database_service.GetAirportsByCity(city)
        if(len(database_airports) == 0):
            airports = self.flight_service.GetAirportsAroundCity(city)
            self.LoadAirportsIntoDatabase(airports)
        
        database_airports = self.__database_service.GetAirportsByCity(city)
        return database_airports[0].Airport.AirportID

    def GetAirportsInCountry(self, country : str):
        return self.__database_service.GetAirportsByCountry(country)

    def GetAirportsInContinent(self, continent : str):
        return self.__database_service.GetAirportsByContinent(continent)

    def SearchResults(self):
        from_city = request.form['From City']
        from_date = request.form['Depart Date']
        to_date = request.form['Return Date']
        destination_type = request.form['Destination Type']
        destination = request.form['Destination']
                      
        if(destination_type == "Continent"):
            refine_destination = "Country"
            to_airports = self.__database_service.GetAirportsByContinent(destination)
            to_destinations = sorted(set([airport.Airport.Country for airport in to_airports]))
        elif(destination_type == "Country"):
            refine_destination = "City"
            to_airports = self.__database_service.GetAirportsByCountry(destination)
            to_destinations = sorted(set([airport.Airport.City for airport in to_airports]))
        elif(destination_type == "Any"):
            refine_destination = "Continent"
            to_airports = self.__database_service.GetAllAirports()
            to_destinations = sorted(set([airport.Airport.Continent for airport in to_airports]))
        else: # destination_type == "City"
            refine_destination = None
            to_airports = self.__database_service.GetAirportsByCity(destination)
            to_destinations = sorted(set([airport.Airport.Continent for airport in to_airports]))

        if(refine_destination is None):
            from_date = datetime.strptime(from_date, "%Y-%m-%d")
            to_date = datetime.strptime(to_date, "%Y-%m-%d")
            self.__flight_viewer.BuildOutgoingFlightView(from_city, destination, from_date)
            self.__flight_viewer.BuildReturnFlightView(from_city, destination, to_date)
            flight_views = self.__flight_viewer.GetFlightViews()
            return render_template('/SearchResults.html', search_criteria=request.form, results=flight_views)
        else:
            return render_template('/DestinationSelection.html', search_criteria=request.form, destinations=to_destinations, destination_type=refine_destination)

    def HomePage(self):
        return render_template('Home.html')

    def Checkout(self):
        tickets = []
        total_price = 0
        if("Departure Ticket" in request.form):
            flight = self.__database_service.GetFlightByID(request.form["Departure Ticket"])[0]
            tickets.append(flight)
            total_price += flight.Flight.Price
        if("Return Ticket" in request.form):
            flight = self.__database_service.GetFlightByID(request.form["Return Ticket"])[0]
            tickets.append(flight)
            total_price += flight.Flight.Price
        return render_template('Checkout.html', tickets=tickets, total_price=total_price)