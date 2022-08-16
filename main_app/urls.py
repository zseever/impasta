from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurants/',  views.RestaurantList.as_view(), name="restaurants_index"),
    path('accounts/signup/', views.signup, name='signup'),
    path('restaurants/<int:pk>/', views.RestaurantDetail.as_view(), name='restaurants_detail'),
    path('restaurants/<int:restaurant_id>/menu/<int:pk>/', views.MenuItemDetail.as_view(), name='menuitems_detail'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipes_detail'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),
    path('recipes/<int:recipe_id>/add_instruction/', views.add_instruction, name='add_instructions'),
    path('recipes/<int:recipe_id>/add_ingredient/', views.add_ingredient, name='add_ingredients'),
    path('ingredients/<int:ingredient_id>/delete/', views.delete_ingredient, name='ingredients_delete'),
    path('instructions/<int:instruction_id>/delete/', views.delete_instruction, name='instructions_delete'),
    path('recipes/<int:recipe_id>/add_review/', views.add_review, name='add_reviews'),
    path('reviews/<int:review_id>/delete/', views.delete_review, name='reviews_delete'),
]