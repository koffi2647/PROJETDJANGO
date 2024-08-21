from django.urls import path
from modifierEleve.views import index

urlpatterns = [
    path('', index),
]