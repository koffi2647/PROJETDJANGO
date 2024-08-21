
from django.urls import path

from professeur.views import index


urlpatterns = [
    path('', index),
]