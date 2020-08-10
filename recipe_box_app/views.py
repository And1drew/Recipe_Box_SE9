from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from recipe_box_app.models import Author, Recipe
from recipe_box_app.forms import add_author_form, add_recipe_form


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


def add_recipe_view(request):
    if request.method == 'POST':
        form = add_recipe_form(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            new_Recipe = Recipe.objects.create(
                title = form.get('title'),
                author = form.get('author'),
                description = form.get('description'),
                time_required = form.get('time_required'),
                instructions = form.get('instructions'),
            )
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = add_recipe_form()
    return render(request, 'add_recipe_view.html',{'form': form})


def add_author_view(request):
    if request.method == 'POST':
        form = add_author_form(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))
    form = add_author_form()
    return render(request, 'add_author_view.html', {'form': form})