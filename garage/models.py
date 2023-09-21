from django.db import models

# Create your models here.
class Garage(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)