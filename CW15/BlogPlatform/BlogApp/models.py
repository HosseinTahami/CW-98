from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

class Post(models.Models):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
    Author,
    on_delete=models.CASCADE
    )
    date = models.DateField(auto_now_add=True)
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now_add=True)

class Category(models.Models):
    name = models.CharField(max_length=200)
    description = models.TextField()


