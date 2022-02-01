from django.db import models

class Calculator(models.Model):
    name = models.TextField(default="placeholder")
    mhs = models.FloatField()
    power = models.IntegerField()
    price = models.FloatField()  # GBP
    kwh_price = models.FloatField()
    efficiency = models.FloatField()
    epp = models.FloatField()
    roi = models.FloatField()
    # year
    # month
    # day
    # week
