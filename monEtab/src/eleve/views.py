from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    context = {
        'title':'mon premier article',
        'title':'contenue du premier article'
    }
    return render(request, "eleves/listeEleve.html")
# Create your views here.
