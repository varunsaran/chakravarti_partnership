from django.urls import path
from . import views

# Defines all url patterns. First has the relative link, then the views function to call, and the url name that can be used later.

urlpatterns = [
    path('old', views.old_home, name = 'blog-old-home'),
    path('about/', views.about, name = 'blog-about'),
    path('', views.home, name = 'blog-home'),
    path('transactions/', views.transactions, name = 'blog-transactions'),
    path('topholdings/', views.top_holdings, name = 'blog-top-holdings'),


]
