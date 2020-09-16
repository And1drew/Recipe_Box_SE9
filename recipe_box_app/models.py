from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=60)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=120, default='')
    password = models.CharField(max_length=120, default='')
    favorites = models.ManyToManyField("Recipe", related_name='favorites')
    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=40)
    instructions = models.TextField()