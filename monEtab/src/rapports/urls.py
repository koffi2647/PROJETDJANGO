from django.urls import path
from rapports.views import index

urlpatterns = [
    path('', index),
]