from tkinter import CASCADE
from django.db import models
from accounts.models import Account
from misc.models import *

class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

class Condition(models.Model):
    condition = models.CharField(max_length=20)

    def __str__(self):
        return self.condition
    
class PropertyType(models.Model):
    p_type = models.CharField(max_length=50)

    def __str__(self):
        return self.p_type
    
class ListingImage(models.Model):
    image = models.ImageField(upload_to="ListingImages")

    
class Listing(models.Model):
    images = models.ManyToManyField(ListingImage, blank=True, null=True)
    agent = models.ForeignKey(Account, models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    negotiable = models.BooleanField(default=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.agent.get_full_name()