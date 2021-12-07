from flask import render_template, request, redirect
# from FlightServices.TestFlightServiceFactory import TestFlightServiceFactory as FlightServiceFactory
from FlightServices.KiwiFlightServiceFactory import KiwiFlightServiceFactory as FlightServiceFactory
from DatabaseServices.PostgresDatabaseServiceFactory import PostgresDatabaseServiceFactory as DatabaseServiceFactory
from DatabaseServices.Database_Schema import Airport
from PeriodicUpdater import PeriodicUpdater
from DisplayServices.FlightViewerBuilder import FlightViewerBuilder
import json
from datetime import datetime

class VacationPlannerFacade():
    def __init__(self) -> render_template:
        self.__flight_service = FlightServiceFactory.CreateFlightServices()
        self.__database_service = DatabaseServiceFactory.CreateDatabaseService()
        self.__periodic_updater = PeriodicUpdater.GetPeriodicUpdater(self.__flight_service, DatabaseServiceFactory.CreateDatabaseService())
        self.__periodic_updater.start()
        self.__flight_viewer = FlightViewerBuilder(self.__flight_service, self.__database_service)

    def ListFlights(self) -> render_template:
        flights = self.__database_service.GetAllFlights()
        return render_template('ListFlights.html', flights=flights)

    def ListAirports(self) -> render_template:
        airports = self.__database_service.GetAllAirports()
        return render_template('ListAirports.html', airports=airports)
    
    def SearchResults(self) -> render_template:
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
            self.__flight_viewer.SeedWithLiveData(from_city, destination, from_date, to_date)
            self.__flight_viewer.BuildFlightView(from_city, destination, from_date)
            flight_views = self.__flight_viewer.GetFlightViews()
            if(len(flight_views["Round Trip"]) == 0):
                return render_template('/TryAgain.html')
            return render_template('/SearchResults.html', search_criteria=request.form, results=flight_views)
        else:
            return render_template('/DestinationSelection.html', search_criteria=request.form, destinations=to_destinations, destination_type=refine_destination)

    def HomePage(self) -> render_template:
        return render_template('Home.html')

    def Checkout(self) -> render_template:
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

    def __LoadAirportsIntoDatabase(self, airports : json) -> None:
        for airport_raw in airports['locations']:
            self.__database_service.AddAirportFromRaw(airport_raw)

    def __GetClosestAirportToCity(self, city : str) -> str:
        database_airports = self.__database_service.GetAirportsByCity(city)
        if(len(database_airports) == 0):
            airports = self.__flight_service.GetAirportsAroundCity(city)
            self.__LoadAirportsIntoDatabase(airports)
        
        database_airports = self.__database_service.GetAirportsByCity(city)
        return database_airports[0].Airport.AirportID

    def __GetAirportsInCountry(self, country : str) -> list:
        return self.__database_service.GetAirportsByCountry(country)

    def __GetAirportsInContinent(self, continent : str) -> list:
        return self.__database_service.GetAirportsByContinent(continent)

