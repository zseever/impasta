from django.contrib import admin
from .models import Restaurant, MenuItem, Recipe, Ingredient, Instruction, Review

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Instruction)
admin.site.register(Review)
