from django.urls import path
from recipe_box_app import views

urlpatterns = [
    path('', views.index),
    path('author/<int:author_id>/', views.author_view),
    path('recipe/<int:recipe_id>/', views.recipe_view),
]