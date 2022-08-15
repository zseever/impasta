from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView

from .models import Restaurant, MenuItem, Recipe, Ingredient, Instruction

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