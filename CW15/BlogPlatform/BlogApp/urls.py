from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name = 'posts'),
    path('categories/', views.category_list, name = 'categories'),
    path('authors/', views.author_list, name = 'authors'),
    path('posts/<int:post_id>/', views.post_details),
    path('categories/<int:category_id>/', views.category_details),
    path('authors/<int:author_id>/', views.author_details)
]