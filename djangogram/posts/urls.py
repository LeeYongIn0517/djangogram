from django.urls import path
from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.posts_create, name='posts_create'),
]