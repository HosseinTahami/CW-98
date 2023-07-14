from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    pic = models.ImageField(upload_to = 'images/', default='default_pic.jpg')
    def __str__(self) -> str:
        return f"{self.name} : {self.bio}"

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self) -> str:
        return f"{self.name} : {self.description}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    Category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    date = models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.title} : {self.content} : {self.author} : {self.date}"
class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE
    )
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.post} : {self.author} : {self.date}"
    






