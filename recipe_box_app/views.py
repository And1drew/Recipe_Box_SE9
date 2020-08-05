from django.shortcuts import render
from recipe_box_app.models import Author, Recipe


def index(request):
    recipe_info = Recipe.objects.all()
    return render(request, 'index.html', {'recipe_data': recipe_info})


def author_view(request, author_id):
    author_info = Author.objects.filter(id=author_id)
    author_info = author_info.first()
    recipe_info = Recipe.objects.filter(id=author_id)
    return render(request, "author_view.html", 
    {'author': author_info, 'recipes': recipe_info})


def recipe_view(request, recipe_id):
    recipe_info = Recipe.objects.filter(id=recipe_id)
    recipe_info = recipe_info.first()
    return render(request, "recipe_view.html", {'recipe': recipe_info})
