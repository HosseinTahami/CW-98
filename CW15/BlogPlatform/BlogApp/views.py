from django.shortcuts import render
from .models import Post, Author, Category
# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'all':posts})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'all':categories})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'all': authors })
    