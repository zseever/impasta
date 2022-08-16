from distutils.log import Log
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Avg
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from operator import itemgetter

from .models import Restaurant, MenuItem, Recipe, Ingredient, Instruction, Review
from .forms import InstructionForm, IngredientForm, ReviewForm

# Create your views here.
def home(request):
    restaurants = Restaurant.objects.all()[:5]
    recipes = [{
            'id':recipe.id,
            'name':recipe.name,
            'img':recipe.img,
            'avg_rating': recipe.review_set.all().aggregate(Avg('rating'))['rating__avg'] if len(recipe.review_set.all()) else 0
    } for recipe in Recipe.objects.all()]
    recipes = sorted(recipes, key=itemgetter('avg_rating'), reverse=True)[:5]
    return render(request,'home.html', { 
        'restaurants':restaurants,
        'recipes':recipes,
    })

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
            return redirect('home')
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
        context['review_form'] = ReviewForm()
        return context


class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['name', 'img', 'time', 'tags', 'menu_item']
    success_url= '/recipes/'
    login_url = 'signup'

    def get_success_url(self) -> str:
        return f'/recipes/{self.object.id}'
 
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = '__all__'
    login_url = 'signup'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = '/'
    login_url = 'signup'

@login_required
def add_instruction(request, recipe_id):
    form = InstructionForm(request.POST)
    if form.is_valid():
        new_instruction = form.save(commit=False)
        new_instruction.recipe_id = recipe_id
        new_instruction.user = request.user
        new_instruction.save()
    return redirect('recipes_detail', pk=recipe_id)

@login_required
def add_ingredient(request, recipe_id):
    form = IngredientForm(request.POST)
    if form.is_valid():
        new_ingredient = form.save(commit=False)
        new_ingredient.recipe_id = recipe_id
        new_ingredient.user = request.user
        new_ingredient.save()
    return redirect('recipes_detail', pk=recipe_id)

@login_required
def delete_ingredient(request, ingredient_id):
    ingredient = Ingredient.objects.get(id=ingredient_id)
    recipe = ingredient.recipe
    if request.user == ingredient.user:
        ingredient.delete()
    return redirect('recipes_detail', pk=recipe.id)

@login_required
def delete_instruction(request, instruction_id):
    instruction = Instruction.objects.get(id=instruction_id)
    recipe = instruction.recipe
    instruction.delete()
    return redirect('recipes_detail', pk=recipe.id)

@login_required
def add_review(request, recipe_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.recipe_id = recipe_id
        new_review.user = request.user
        new_review.save()
    return redirect('recipes_detail', pk=recipe_id)

@login_required
def delete_review(request, review_id):
    review = Review.objects.get(id=review_id)
    recipe = review.recipe
    review.delete()
    return redirect('recipes_detail', pk=recipe.id)