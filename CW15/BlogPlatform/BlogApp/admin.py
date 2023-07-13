from django.contrib import admin
from .models import Author, Post, Comment, Category
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Author)

