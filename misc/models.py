from django.db import models

class Country(models.Model):
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.country

class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.CharField(max_length=20)

    def __str__(self):
        return self.region

class Area(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    area = models.CharField(max_length=50)

    def __str__(self):
        return self.area