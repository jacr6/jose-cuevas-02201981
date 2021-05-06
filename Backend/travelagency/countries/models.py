from djongo import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    centseparator = models.CharField(max_length=100)
    millionseparator = models.CharField(max_length=100)
    locale = models.CharField(max_length=100)
    decimals = models.CharField(max_length=100)
    displaysymbol = models.CharField(max_length=100)

 