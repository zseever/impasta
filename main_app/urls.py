from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurants/',  views.RestaurantList.as_view(), name="restaurants_index"),
    path('accounts/signup/', views.signup, name='signup'),
    path('restaurants/<int:pk>/', views.RestaurantDetail.as_view(), name='restaurants_detail'),
    path('restaurants/<int:restaurant_id>/menu/<int:pk>/', views.MenuItemDetail.as_view(), name='menuitems_detail'),
]