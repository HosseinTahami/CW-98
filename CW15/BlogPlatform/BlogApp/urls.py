from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list) ,
    path('categories/', views.category_list) ,
    path('authors/', views.author_list) 
]