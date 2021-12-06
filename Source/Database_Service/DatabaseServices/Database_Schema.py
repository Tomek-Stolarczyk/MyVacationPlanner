from sqlalchemy import Column, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Flight(Base):
    __tablename__ = 'Flight'

    FlightID    = Column(String(100), primary_key=True)
    Date        = Column(Date())
    AirportTo   = Column(String(5))
    AirportFrom = Column(String(5))
    Price       = Column(Numeric(11,2))

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
