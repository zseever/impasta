from django.forms import ModelForm
from .models import Instruction, Ingredient

class InstructionForm(ModelForm):
  class Meta:
    model = Instruction
    fields = ['order', 'step']

class IngredientForm(ModelForm):
  class Meta:
    model = Ingredient
    fields = ['quantity', 'name']