from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
class Comment(models.Model):
    post = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


