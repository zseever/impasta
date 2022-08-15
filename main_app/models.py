from ctypes import addressof
from pydoc import describe
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
        return f'{self.restaurant.name}\'s {self.name}'



class Recipe(models.Model):
    name = models.CharField(max_length=250, verbose_name="Recipe Name")
    img = models.CharField(max_length=250, verbose_name="Image URL")
    time = models.CharField(max_length=250, verbose_name="Prep Time")
    tags = models.CharField(max_length=250, verbose_name="Tags")
    menu_item = models.ManyToManyField(MenuItem, verbose_name="Related Menu Item(s)")

    def get_absolute_url(self):
        return reverse('recipes_detail', kwargs={'recipe_id' : self.id})
    
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

class Review(models.Model):
    RATINGS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    rating = models.IntegerField(default=5, choices=RATINGS)
    comment = models.TextField(max_length=2500)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )

