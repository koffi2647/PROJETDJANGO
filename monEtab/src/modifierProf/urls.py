from django.urls import path
from modifierProf.views import index

urlpatterns = [
    path('', index),
]