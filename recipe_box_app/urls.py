from django.urls import path
from recipe_box_app import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('author/<int:author_id>/', views.author_view),
    path('recipe/<int:recipe_id>/', views.recipe_view),
    path('add_recipe/', views.add_recipe_view),
    path('add_author/', views.add_author_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('forbidden/', views.forbidden_view)
]