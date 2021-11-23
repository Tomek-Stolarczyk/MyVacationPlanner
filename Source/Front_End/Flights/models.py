from django.db import models
from django.db.models.fields.related import ForeignKey
from djmoney.models.fields import MoneyField

# Create your models here.
class Flights(models.Model):
    FlightID    = models.CharField(max_length=10, primary_key=True)
    FromDate    = models.DateField()
    ToDate      = models.DateField()
    AirportTo   = models.CharField(max_length=5)
    AirportFrom = models.CharField(max_length=5)
    Price       = MoneyField(decimal_places=2, default=0,         
                             default_currency='USD', max_digits=11,)


class Airports(models.Model):
    AirportID   = models.CharField(max_length=5, primary_key=True)
    City        = models.CharField(max_length=100)
    State       = models.CharField(max_length=100)
    Country     = models.CharField(max_length=100)
    Continent   = models.CharField(max_length=100)