from django.urls import path

from .views import index, solve


urlpatterns = [
    path('', index),
    path('<str:text>', solve),
]