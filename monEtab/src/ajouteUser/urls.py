from django.urls import path
from ajouteUser.views import index

urlpatterns = [
    path('', index),
]