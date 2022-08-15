from ctypes import addressof
from pydoc import describe
from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=250)
    phone = models.CharField(max_length=20)
    cuisine = models.CharField(max_length=20)
    desc = models.TextField(max_length=1000)
    img = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name} ({self.id})'


class MenuItem(models.Model):
    name = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    price = models.IntegerField()
    desc = models.TextField(max_length=1000)
    img = models.CharField(max_length=250)
    restaurant = models.ForeignKey(
        Restaurant, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Added {self.name} ({self.price}) to {self.restaurant}'

