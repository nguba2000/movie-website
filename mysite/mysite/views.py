from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('<h1 style="color: red; background: black;">This is the home page</h1>') 