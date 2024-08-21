from django.urls import path
from eleve.views import index

urlpatterns = [
    path('', index),
]