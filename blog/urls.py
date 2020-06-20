from django.urls import path
from . import views

urlpatterns = [
    path('old', views.old_home, name = 'blog-old-home'),
    path('about/', views.about, name = 'blog-about'),
    path('', views.home, name = 'blog-home'),
    path('transactions/', views.transactions, name = 'blog-transactions'),

]
