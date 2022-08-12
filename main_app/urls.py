from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurants/',  views.RestaurantList.as_view(), name="restaurant_index"),
    path('accounts/signup/', views.signup, name='signup'),
]