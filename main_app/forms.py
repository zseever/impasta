from django.forms import ModelForm
from .models import Instruction, Ingredient, Review

class InstructionForm(ModelForm):
  class Meta:
    model = Instruction
    fields = ['order', 'step']

class IngredientForm(ModelForm):
  class Meta:
    model = Ingredient
    fields = ['quantity', 'name']

class ReviewForm(ModelForm):
  class Meta:
    model = Review
    fields = ['rating', 'comment']