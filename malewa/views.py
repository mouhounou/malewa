from django.shortcuts import render
from django.http import  HttpResponse
from .models import plat

# Create your views here.

def index(request):
    return render(request, 'malewa/index.html')

def plats(request):
    plats = plat.objects.all()
    return render(request, 'malewa/plats.html', {'plats': plats})
