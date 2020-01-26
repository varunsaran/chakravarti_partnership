from django.urls import path
from . import views

urlpatterns = [
    path('old', views.home, name = 'blog-old-home'),
    path('about/', views.about, name = 'blog-about'),
    path('', views.new_home, name = 'blog-home'),
]