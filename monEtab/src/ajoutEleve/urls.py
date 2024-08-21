from django.urls import path
from ajoutEleve.views import index

urlpatterns = [
    path('', index),
]