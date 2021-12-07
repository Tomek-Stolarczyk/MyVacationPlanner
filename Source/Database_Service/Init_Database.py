from DatabaseServices.Database_Schema import Flight, Airport, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# This is a starter file used to clear out the database and reset it.
# Useful for when the database schema changes


db_user = 'root'
db_pass = 'vacationplanner'
db_name = db_user
db_host = 'db'
db_port = '5432'
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
engine = create_engine(db_string, echo=True)
session = sessionmaker(bind=engine)()

Airports = [
    Airport(
        AirportID="JNU",
        City="Juneau",
        State="Alaska",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="FAI",
        City="Fairbanks",
        State="Alaska",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="PHX",
        City="Phoenix",
        State="Arizona",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="TUS",
        City="Tucson",
        State="Arizona",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="LIT",
        City="Little Rock",
        State="Arkansas",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="XNA",
        City="Fayetteville",
        State="Arkansas",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="LAX",
        City="Los Angeles",
        State="California",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="SFO",
        City="San Francisco",
        State="California",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="DEN",
        City="Denver",
        State="Colorado",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="COS",
        City="Colorado Springs",
        State="Colorado",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="BDL",
        City="Hartford",
        State="Connecticut",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="HVN",
        City="New Haven",
        State="Connecticut",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="ILG",
        City="Wilmington",
        State="Delaware",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="DOV",
        City="Dover",
        State="Delaware",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="MCO",
        City="Orlando",
        State="Florida",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="MIA",
        City="Miami",
        State="Florida",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="ATL",
        City="Atlanta",
        State="Georgia",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="SAV",
        City="Savannah",
        State="Georgia",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="HNL",
        City="Honolulu",
        State="Hawaii",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="OGG",
        City="Kahului",
        State="Hawaii",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="BOI",
        City="Boise",
        State="Idaho",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="IDA",
        City="Idaho Falls",
        State="Idaho",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="MDW",
        City="Chicago",
        State="Illinois",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="ORD",
        City="Chicago",
        State="Illinois",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="IND",
        City="Indianapolis",
        State="Indiana",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="SBN",
        City="South Bend",
        State="Indiana",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="DSM",
        City="Des Moines",
        State="Iowa",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="CID",
        City="Cedar Rapids",
        State="Iowa",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="ICT",
        City="Wichita",
        State="Kansas",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="MHK",
        City="Manhattan",
        State="Kansas",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="CVG",
        City="Cincinnati",
        State="Kentucky",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="SDF",
        City="Louisville",
        State="Kentucky",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="MSY",
        City="New Orleans",
        State="Louisiana",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="BTR",
        City="Baton Rouge",
        State="Louisiana",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="PWM",
        City="Portland",
        State="Maine",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="BGR",
        City="Bangor",
        State="Maine",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="BWI",
        City="Baltimore",
        State="Maryland",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="SBY",
        City="Salisbury",
        State="Maryland",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="BOS",
        City="Boston",
        State="Massachusetts",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="ACK",
        City="Nantucket",
        State="Massachusetts",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="DTW",
        City="Detroit",
        State="Michigan",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="GRR",
        City="Grand Rapids",
        State="Michigan",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="MSP",
        City="Minneapolis",
        State="Minnesota",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="DLH",
        City="Duluth",
        State="Minnesota",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="JAN",
        City="Jackson",
        State="Mississippi",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="GPT",
        City="Gulfport",
        State="Mississippi",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="STL",
        City="St. Louis",
        State="Missouri",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="MCI",
        City="Kansas City",
        State="Missouri",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="BZN",
        City="Bozeman",
        State="Montana",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="BIL",
        City="Billings",
        State="Montana",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="OMA",
        City="Omaha",
        State="Nebraska",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="LNK",
        City="Lincoln",
        State="Nebraska",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="LAS",
        City="Las Vegas",
        State="Nevada",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="RNO",
        City="Reno",
        State="Nevada",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="MHT",
        City="Manchester",
        State="New Hampshire",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="PSM",
        City="Portsmouth",
        State="New Hampshire",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="EWR",
        City="New York",
        State="New Jersey",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="ACY",
        City="Atlantic City",
        State="New Jersey",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="ABQ",
        City="Albuquerque",
        State="New Mexico",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="SAF",
        City="Santa Fe",
        State="New Mexico",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="JFK",
        City="New York",
        State="New York",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="LGA",
        City="New York",
        State="New York",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="CLT",
        City="Charlotte",
        State="North Carolina",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="RDU",
        City="Raleigh",
        State="North Carolina",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="FAR",
        City="Fargo",
        State="North Dakota",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="BIS",
        City="Bismarck",
        State="North Dakota",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="CLE",
        City="Cleveland",
        State="Ohio",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="CMH",
        City="Columbus",
        State="Ohio",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="TUL",
        City="Tulsa",
        State="Oklahoma",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="OKC",
        City="Oklahoma City",
        State="Oklahoma",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="PDX",
        City="Portland",
        State="Oregon",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="EUG",
        City="Eugene",
        State="Oregon",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="PHL",
        City="Philadelphia",
        State="Pennsylvania",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="PIT",
        City="Pittsburgh",
        State="Pennsylvania",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="PVD",
        City="Providence",
        State="Rhode Island",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="BID",
        City="Block Island",
        State="Rhode Island",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="GSP",
        City="Greenville",
        State="South Carolina",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="CHS",
        City="Charleston",
        State="South Carolina",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="FSD",
        City="Sioux Falls",
        State="South Dakota",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="RAP",
        City="Rapid City",
        State="South Dakota",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="BNA",
        City="Nashville",
        State="Tennessee",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="MEM",
        City="Memphis",
        State="Tennessee",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="DFW",
        City="Dallas",
        State="Texas",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="IAH",
        City="Houston",
        State="Texas",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="SLC",
        City="Salt Lake City",
        State="Utah",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="PVU",
        City="Provo",
        State="Utah",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="BTV",
        City="Burlington",
        State="Vermont",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="RUT",
        City="Rutland",
        State="Vermont",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="IAD",
        City="Washington, D.C.",
        State="Virginia",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="DCA",
        City="Washington, D.C.",
        State="Virginia",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="SEA",
        City="Seattle",
        State="Washington",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="GEG",
        City="Spokane",
        State="Washington",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="CRW",
        City="Charleston",
        State="West Virginia",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="HTS",
        City="Huntington",
        State="West Virginia",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="MKE",
        City="Milwaukee",
        State="Wisconsin",
        Country="United States",
        Continent="North America"
    ),
    Airport(
        AirportID="MSN",
        City="Madison",
        State="Wisconsin",
        Country="United States",
        Continent="North America"
    )
]

# state=None
# if(location["city"]["subdivision"] is not None):
#     state = location["city"]["subdivision"]["name"]
# airport = Airport(AirportID=location["code"],
#                   City=location["city"]["name"],
#                   State=state,
#                   Country=location["city"]["country"]["name"],
#                   Continent=location["city"]["continent"]["name"])

def PopulateAirports():
    for airport in Airports:
        try:
            session.add(airport)
            
        except Exception as e:
            print(e)
        print("{\n %s }" % airport)
        session.commit()

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
PopulateAirports()