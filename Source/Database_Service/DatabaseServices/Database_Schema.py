from sqlalchemy import Column, String, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base

# This is the schema that the database uses to communicate 
# with the rest of the system. If you create an instance of
# this class, you can manipulate the underlying database

Base = declarative_base()
class Flight(Base):
    __tablename__ = 'Flight'

    FlightID    = Column(String(100), primary_key=True)
    Date        = Column(DateTime())
    AirportTo   = Column(String(5))
    AirportFrom = Column(String(5))
    Price       = Column(Numeric(11,2))
    BookingLink = Column(String(2000))

    def __repr__(self):
        return '<Flight %r>' % self.FlightID

class Airport(Base):
    __tablename__ = 'Airport'
    AirportID    = Column(String(5), primary_key=True)
    City         = Column(String(100))
    State        = Column(String(100))
    Country      = Column(String(100))
    Continent    = Column(String(100))

    def __repr__(self):
        return '<Airport %r>' % self.AirportID
    
    def __str__(self):
        airport_str = "Code: %s\n" % self.AirportID
        airport_str += "City: %s\n" % self.City
        if(self.State != ""):
            airport_str += "State %s\n" % self.State
        airport_str += "Country %s\n" % self.Country
        airport_str += "Continent %s\n" % self.Continent
        return airport_str
