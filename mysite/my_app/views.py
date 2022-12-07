from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def movies(request):
    return render(request, 'movies.html')

def register(request):
    return render(request, 'register.html')

def theaters(request):
    return render(request, 'theaters.html')