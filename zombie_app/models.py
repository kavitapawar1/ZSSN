from django.db import models

# Create your models here.

class Survivor(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    longitude = models.FloatField()
    latitude = models.FloatField()
    is_infected = models.BooleanField(default=False)
        
    def __str__(self):
        return self.name