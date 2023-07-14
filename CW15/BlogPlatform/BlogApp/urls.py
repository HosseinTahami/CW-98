from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list),
    path('categories/', views.category_list),
    path('authors/', views.author_list),
    path('<int:post_id>/', views.post_details),
    path('<int:category_id/', views.category_details),
    path('<int:author_id>/', views.author_details)
]