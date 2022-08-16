from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Avg

from .models import Restaurant, MenuItem, Recipe, Ingredient, Instruction
from .forms import InstructionForm, IngredientForm

# Create your views here.
def home(request):
    restaurants = Restaurant.objects.all()[:5]
    # Render 5 restaurants - image + Name
    return render(request,'home.html', { 'restaurants':restaurants})

class RestaurantList(ListView):
    model = Restaurant
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(RestaurantList, self).get_context_data(**kwargs)
        context['cuisines'] = ['American','Chinese','Indian','Italian','Other']
        return context

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class RestaurantDetail(DetailView):
    model = Restaurant
    fields = '__all__'


class MenuItemDetail(DetailView):
    model = MenuItem
    fields = '__all__'

    @property
    def menu_item(self):
        return self.kwargs['pk'] 

    def get_context_data(self, **kwargs):
        context = super(MenuItemDetail, self).get_context_data(**kwargs)
        recipes_set = MenuItem.objects.get(id=self.menu_item).recipe_set.all()
        recipes = [{
            'id':recipe.id,
            'name':recipe.name,
            'img':recipe.img,
            'time':recipe.time,
            'avg_rating':recipe.review_set.all().aggregate(Avg('rating'))['rating__avg']
        } for recipe in recipes_set]
        context['recipes'] = recipes
        return context

class RecipeDetail(DetailView):
    model = Recipe
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(RecipeDetail, self).get_context_data(**kwargs)
        context['instruction_form'] = InstructionForm()
        context['ingredient_form'] = IngredientForm()
        return context

class RecipeCreate(CreateView):
    model = Recipe
    fields = '__all__'
    success_url= '/recipes/'

    def get_success_url(self) -> str:
        return f'/recipes/{self.object.id}'

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = '__all__'

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/'


def add_instruction(request, recipe_id):
    form = InstructionForm(request.POST)
    if form.is_valid():
        new_instruction = form.save(commit=False)
        new_instruction.recipe_id = recipe_id
        new_instruction.save()
    return redirect('recipes_detail', pk=recipe_id)

def add_ingredient(request, recipe_id):
    form = IngredientForm(request.POST)
    if form.is_valid():
        new_ingredient = form.save(commit=False)
        new_ingredient.recipe_id = recipe_id
        new_ingredient.save()
    return redirect('recipes_detail', pk=recipe_id)

def delete_ingredient(request, ingredient_id):
    ingredient = Ingredient.objects.get(id=ingredient_id)
    recipe = ingredient.recipe
    ingredient.delete()
    return redirect('recipes_detail', pk=recipe.id)

def delete_instruction(request, instruction_id):
    instruction = Instruction.objects.get(id=instruction_id)
    recipe = instruction.recipe
    instruction.delete()
    return redirect('recipes_detail', pk=recipe.id)