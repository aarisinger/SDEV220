from django.db import models

# Create your models here.
class Car(models.Model):
    FUELTYPE = [
        ('', 'choose one'),
        ('gas', 'Gas'), 
        ('diesel', 'Diesel'),
        ('hybrid', 'Hybrid'),
        ('lp_gas', 'LP Gas')
    ]
    ROOFTYPE = [
        ('', 'choose one'),
        ('sunroof', 'Sunroof'),
        ('convertable', 'Convertable'),
        ('solid roof', 'Solid Roof')
    ]
    vin = models.CharField(max_length=20)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    numDoors = models.PositiveSmallIntegerField()
    roofType = models.CharField(max_length=50, choices=ROOFTYPE, default='')
    year = models.PositiveSmallIntegerField()
    fuelType = models.CharField(max_length=50, choices=FUELTYPE, default='')

    def __str__(self):
        return f"{self.color} {self.make} {self.model}"