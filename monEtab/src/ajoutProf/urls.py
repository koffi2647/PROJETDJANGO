from django.urls import path
from ajoutProf.views import index

urlpatterns = [
    path('', index),
]