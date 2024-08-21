from django.urls import path
from modifUser.views import index

urlpatterns = [
    path('', index),
]