from DatabaseServices.Database_Schema import Airport, Flight
from DatabaseServices.IDatabaseService import IDatabaseService

from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
import json
from datetime import datetime

# The real meat of the database service. This service uses a sister 
# postgres database to store and get data.
class PostgresDatabaseService(IDatabaseService):
    def __init__(self):
        db_user = 'root'
        db_pass = 'vacationplanner'
        db_name = db_user
        db_host = 'db'
        db_port = '5432'
        db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
        # Create an engine and a session. Each thread should have their
        # own session so postgres can make sure that data is flowing in
        # and out in a consisent manner.
        engine = create_engine(db_string, echo=True)
        self.session = sessionmaker(bind=engine)()        

    def AddAirport(self, airport : Airport) -> None:
        try:
            self.session.add(airport)
            self.session.commit()
        except:
            # Sometimes this happens when we try to input an airport
            # that already exists in the system. Just rollback the
            # request since there's nothing in the airport model that
            # should need updating
            self.session.rollback()

    def AddFlight(self, flight : Flight) -> None:
        try:
            self.session.add(flight)
            self.session.commit()
        except:
            # Unlike the AddAirport, if we fail to input a flight here,
            # we may have hit an existing flight, but things may have changed
            # like price or booking link. Look for the existing flight and
            # update it's entry
            self.session.rollback()
            existing_flight = self.session.execute(self.session.query(Flight).filter_by(FlightID=flight.FlightID)).fetchone()
            existing_flight.Flight.Date = flight.Date
            existing_flight.Flight.AirportTo = flight.AirportTo
            existing_flight.Flight.AirportFrom = flight.AirportFrom
            existing_flight.Flight.Price = flight.Price
            existing_flight.Flight.BookingLink = flight.BookingLink
            self.session.commit()

    def AddFlightFromRaw(self, raw_flight : json) -> None:
        # This method is useful for adding flights right from the
        # request content that came from the IFlightService. That way
        # we don't need to create a Flight object outside and call AddFlight.
        from_date = datetime.strptime(raw_flight['utc_arrival'], "%Y-%m-%dT%H:%M:%S.000Z")
        new_flight = Flight(
            FlightID     = raw_flight['id'][:100],
            Date         = from_date,
            AirportTo    = raw_flight['flyTo'],
            AirportFrom  = raw_flight['flyFrom'],
            Price        = raw_flight['price'],
            BookingLink  = raw_flight['deep_link'])
        self.AddFlight(new_flight)

    def AddAirportFromRaw(self, raw_airport : json) -> None:
        # Similar to add flight but instead, add an airport.
        # Handle some trickiness where the state is sometimes in a
        # weird spot.
        state=None
        if("city" in raw_airport and
           "subdivision" in raw_airport["city"] and 
           raw_airport["city"]["subdivision"] is not None):
            state = raw_airport["city"]["subdivision"]["name"]
        elif("subdivision" in raw_airport and 
            raw_airport["subdivision"] is not None):
            state = raw_airport["subdivision"]["name"]

        #  Sometimes the Country is also in a weird spot.
        country = None
        if("country" in raw_airport):
            country = raw_airport["country"]["name"]
        else:
            country = raw_airport["city"]["country"]["name"]

        # Can never be too safe, do the same for continents
        continent = None
        if ("continent" in raw_airport):
            continent = raw_airport["continent"]["name"]
        else:
            continent = raw_airport["city"]["continent"]["name"]

        new_airport = Airport(
            AirportID    = raw_airport['code'],
            City         = raw_airport['city']['name'],
            State        = state,
            Country      = country,
            Continent    = continent
        )
        self.AddAirport(new_airport)

    # Following methods are self documenting as the statement is similar
    # in syntax to a typical SQL statement
    def GetAirportsByContinent(self, continent : str) -> list:
        statement = select(Airport).filter_by(Continent=continent)
        return self.session.execute(statement).all()

    def GetAirportsByCountry(self, country : str) -> list:
        statement = select(Airport).filter_by(Country=country)
        return self.session.execute(statement).all()

    def GetAirportsByCity(self, city : str) -> list:
        statement = select(Airport).filter_by(City=city)
        return self.session.execute(statement).all()
    
    def GetAirportByID(self, airportID : str) -> list:
        statement = select(Airport).filter_by(AirportID=airportID)
        return self.session.execute(statement).all()
    
    def GetAllAirports(self) -> list:
        return self.session.execute(select(Airport)).all()

    def GetAllFlights(self) -> list:
        return self.session.execute(select(Flight)).all()

    # Get Flights that are going between 2 airports
    def GetFlights(self, from_airport : str, to_airport : str, departure_date : str, limit=10) -> list:
        statement = select(Flight).filter_by(AirportTo=to_airport, AirportFrom=from_airport)
        return self.session.execute(statement).fetchmany(limit)

    def GetRandomAirport(self) -> list:
        return self.session.execute(select(Airport).order_by(func.random())).fetchone()

    def GetFlightByID(self, flight_id : str) -> list:
        statement = select(Flight).filter_by(FlightID=flight_id)
        return self.session.execute(statement).all()