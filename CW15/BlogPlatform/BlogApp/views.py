from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Category, Comment

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

def author_details(request, author_id):
    detail = Author.objects.get(id = author_id)
    return render(request, 'author_details.html', {'detail': detail})

def post_details(request, post_id):
    detail = get_object_or_404(Post, id = post_id)
    comment = list(Comment.objects.all())
    res2 = list()
    for item in comment:
        if item.post.title == detail.title:
            res2.append(item)
            
    return render(request, 'post_details.html', {'detail': detail , 'comment':res2})

def category_details(request, category_id):
    detail = Category.objects.get(id = category_id)
    return render(request, 'category_details.html', {'detail': detail})