from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list),
    path('categories/', views.category_list),
    path('authors/', views.author_list),
    path('posts/<int:post_id>/', views.post_details),
    path('categories/<int:category_id', views.category_details),
    path('authors/<author_id:int>/', views.author_details)
]