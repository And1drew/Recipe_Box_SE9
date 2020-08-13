from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=60)
    bio = models.TextField()
    username = models.CharField(max_length=120, default='')
    password = models.CharField(max_length=120, default='')
    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=40)
    instructions = models.TextField()