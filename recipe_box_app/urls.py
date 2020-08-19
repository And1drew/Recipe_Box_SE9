from django.urls import path
from recipe_box_app import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('author/<int:author_id>/', views.author_view),
    path('recipe/<int:recipe_id>/', views.recipe_view),
    path('addrecipe/', views.add_recipe),
    path('addauthor/', views.add_author),
]