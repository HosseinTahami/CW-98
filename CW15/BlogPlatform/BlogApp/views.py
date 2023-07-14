from django.shortcuts import render
from .models import Post
# Create your views here.
def show_posts(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'all':posts})

def show_categories(request):
    pass

def show_authors(request):
    pass