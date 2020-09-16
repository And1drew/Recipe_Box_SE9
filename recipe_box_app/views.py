from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from recipe_box_app.models import Author, Recipe
from recipe_box_app.forms import add_author_form, add_recipe_form, login_form

# got help from Andrew Belanger (Jack Detke's comment)
def index(request):
    recipe_info = Recipe.objects.all()
    return render(request, 'index.html', {'recipe_data': recipe_info})

def author_view(request, author_id):
    author_info = Author.objects.filter(id=author_id)
    author_info = author_info.first()
    recipe_info = Recipe.objects.filter(author=author_id)
    return render(request, "author_view.html", 
    {'author': author_info, 'recipes': recipe_info})

def recipe_view(request, recipe_id):
    recipe_info = Recipe.objects.filter(id=recipe_id)
    recipe_info = recipe_info.first()
    return render(request, "recipe_view.html", {'recipe': recipe_info})

def favorites_view(request):
    user_favorites = request.user.author.favorites.all()
    return render(request, 'favorites.html', {'favorites': user_favorites})

def add_favorite_view(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    request.user.author.favorites.add(recipe)
    request.user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def remove_favorite_view(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    request.user.author.favorites.remove(recipe)
    request.user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required()
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
    return render(request, 'generic_form.html',{'form': form})

# got some help from Andrew Belanger (Jack Detke's comment)
@login_required()
def edit_recipe_view(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id).first()
    if not request.user.is_staff:
        if not recipe.author == request.user.author:
            return HttpResponseRedirect('/forbidden')
    if request.method == "POST":
        form = add_recipe_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe.title = data['title']
            recipe.description = data['description']
            recipe.time_required = data['time_required']
            recipe.save()
            return HttpResponseRedirect('/')
    data = {
        'title': recipe.title,
        'description': recipe.description,
        'time_required': recipe.time_required,
        'instructions': recipe.instructions
    }
    form = add_recipe_form(initial=data)
    return render(request, 'generic_form.html', {'form': form})


def add_author_view(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/forbidden')
    if request.method == 'POST':
        form = add_author_form(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            userobject = User.objects.create_user(username=form.get('username'), password=form.get('password'))
            new_Author = Author.objects.create(
                name = form.get('name'),
                bio = form.get('bio'),
                user = userobject,
                username = form.get('username'),
                password = form.get('password'),
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = add_author_form()
    return render(request, 'generic_form.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            user = authenticate(request, username=form.get('username'), password=form.get('password'))
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next', '/'))
    form = login_form
    return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def forbidden_view(request):
    return render(request, 'forbidden.html')