from DatabaseServices.Database_Schema import Airport, Flight
from DatabaseServices.IDatabaseService import IDatabaseService

from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
import json
from datetime import datetime

class PostgresDatabaseService(IDatabaseService):
    def __init__(self):
        db_user = 'root'
        db_pass = 'vacationplanner'
        db_name = db_user
        db_host = 'db'
        db_port = '5432'
        db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
        engine = create_engine(db_string, echo=True)
        self.session = sessionmaker(bind=engine)()        

    def AddAirport(self, airport : Airport):
        try:
            self.session.add(airport)
            self.session.commit()
        except:
            self.session.rollback()

    def AddFlight(self, flight : Flight):
        self.session.add(flight)
        self.session.commit()

    def AddFlightFromRaw(self, raw_flight : json):
        from_date = datetime.strptime(raw_flight['utc_arrival'], "%Y-%m-%dT%H:%M:%S.000Z")
        new_flight = Flight(
            FlightID     = raw_flight['id'][:100],
            Date         = from_date,
            AirportTo    = raw_flight['flyTo'],
            AirportFrom  = raw_flight['flyFrom'],
            Price        = raw_flight['price'])
        self.AddFlight(new_flight)

    def AddAirportFromRaw(self, raw_airport : json):
        state=None
        if("city" in raw_airport and
           "subdivision" in raw_airport["city"] and 
           raw_airport["city"]["subdivision"] is not None):
            state = raw_airport["city"]["subdivision"]["name"]
        elif("subdivision" in raw_airport and 
            raw_airport["subdivision"] is not None):
            state = raw_airport["subdivision"]["name"]

        country = None
        if("country" in raw_airport):
            country = raw_airport["country"]["name"]
        else:
            country = raw_airport["city"]["country"]["name"]

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

    def GetAirportsByContinent(self, continent : str):
        statement = select(Airport).filter_by(Continent=continent)
        return self.session.execute(statement).all()

    def GetAirportsByCountry(self, country : str):
        statement = select(Airport).filter_by(Country=country)
        return self.session.execute(statement).all()

    def GetAirportsByCity(self, city : str):
        statement = select(Airport).filter_by(City=city)
        return self.session.execute(statement).all()
    
    def GetAirportByID(self, airportID : str):
        statement = select(Airport).filter_by(AirportID=airportID)
        return self.session.execute(statement).all()
    
    def GetAllAirports(self):
        return self.session.execute(select(Airport)).all()

    def GetAllFlights(self):
        return self.session.execute(select(Flight)).all()

    def GetFlights(self, from_airport : str, to_airport : str, departure_date : str, limit=10):
        statement = select(Flight).filter_by(AirportTo=to_airport, AirportFrom=from_airport)
        return self.session.execute(statement).fetchmany(limit)

    def GetRandomAirport(self):
        return self.session.execute(select(Airport).order_by(func.random())).fetchone()

    def GetFlightByID(self, flight_id):
        statement = select(Flight).filter_by(FlightID=flight_id)
        return self.session.execute(statement).all()