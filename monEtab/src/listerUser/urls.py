from django.urls import path
from listerUser.views import index

urlpatterns = [
    path('', index),
]