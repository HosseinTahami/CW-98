from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Comment
from users.models import Author
from django.http import HttpResponse


# Create your views here.


def home(request):
    # visited = request.COOKIES.get('visited')
    # if visited:
    #     context={'welcoming' : 'Welcome back !'}
    # else:
    #     context={'welcoming' : 'Welcome to my Website !'}
    #     response.set_cookie('visited', True)
    context = {}
    if request.method == "GET" :
        if request.GET.get('sub') :
            searched = request.GET.get('searched')
            result = Post.objects.filter(Q(title__icontains=searched) | Q(content__icontains=searched)).distinct()
            context['results'] = result
            context['searched'] =  searched
        else:
            return render(request, 'base.html',context)
            
    return render(request, 'index.html', context)
    
def post_list(request):
    all_posts = Post.objects.all()
    return render(request, "Blog/post_list.html", {"all_posts": all_posts})


def post_details(request, pk):
    context = {}
    if request.method == 'GET':
        post = Post.objects.get(id=pk)
        comments = Comment.objects.filter(Q(post__id=pk))
        if request.GET.get('sub') :
            author_comment = request.GET.get('author')
            content_comment = request.GET.get('content')
            author_obj = Author.objects.get(name=author_comment)
            Comment.objects.create(
                author_id=author_obj.id,
                content=content_comment,
                post_id=pk)
            print(author_comment)
        context = {"post": post,
                   "comments":comments
                   }
        
    return render(request, "Blog/post.html", context)


def category_list(request):
    if request.GET.get('sub'):
        name = request.GET.get('name')
        description = request.GET.get('description')
        Category.objects.create(
            name=name,
            description=description
        )
        print(name)
    all_category = Category.objects.all()
    return render(request, "Blog/category_list.html", {"all_category": all_category})


def category_details(request, pk):
    category = Category.objects.get(id=pk)
    return render(request, "Blog/category_details.html", {"category": category })
