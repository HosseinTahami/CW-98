from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.show_posts) ,
    path('categories/', views.show_categories) ,
    path('authors/', views.show_authors) 
]