from django.db import models


class CarModel(models.Model):
    brand = models.CharField(max_length=25)
    year = models.IntegerField()
    number_of_seats = models.IntegerField()
    type_body = models.CharField(max_length=25)
    engine = models.FloatField()
