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



class Recipe(models.Model):
    name = models.CharField(max_length=250)
    img = models.CharField(max_length=250)
    time = models.CharField(max_length=250)
    tags = models.CharField(max_length=250)
    menu_item = models.ManyToManyField(MenuItem)
    
class Instruction(models.Model):
    order = models.IntegerField()
    step = models.TextField(max_length=2500)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )

class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    quantity = models.CharField(max_length=250)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )