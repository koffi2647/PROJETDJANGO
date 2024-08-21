from django.urls import path
from connection.views import index

urlpatterns = [
    path('', index),
]