from django.urls import path

# 'from . import x' means import relative to this file - __init__.py made this directory a module
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('books/', views.books, name='books')
]
