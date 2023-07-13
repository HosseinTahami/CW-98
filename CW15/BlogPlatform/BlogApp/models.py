from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self) -> str:
        return f"{self.name} : {self.bio}"
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.title} : {self.content} : {self.author} : {self.date}"
    
class Comment(models.Model):
    post = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.post} : {self.author} : {self.date}"

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self) -> str:
        return f"{self.name} : {self.description}"

